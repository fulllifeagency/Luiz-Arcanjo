const RECIPIENT = "assessorialuizarcanjo@gmail.com";

function clean(value, max = 1200) {
  return String(value || "").replace(/\0/g, "").trim().slice(0, max);
}

function html(value) {
  return clean(value, 4000)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;")
    .replace(/\n/g, "<br>");
}

function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" }
  });
}

export async function onRequestPost(context) {
  const requestOrigin = context.request.headers.get("origin");
  const ownOrigin = new URL(context.request.url).origin;
  if (requestOrigin && requestOrigin !== ownOrigin) return json({ error: "Origem inválida." }, 403);

  let data;
  try {
    data = await context.request.json();
  } catch {
    return json({ error: "Dados inválidos." }, 400);
  }

  if (clean(data.company)) return json({ ok: true });

  const nome = clean(data.nome, 120);
  const email = clean(data.email, 180).toLowerCase();
  const assunto = clean(data.assunto, 120);
  const mensagem = clean(data.mensagem, 5000);
  if (!nome || !assunto || !mensagem || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return json({ error: "Preencha nome, e-mail, assunto e mensagem." }, 422);
  }
  if (!context.env.RESEND_API_KEY || !context.env.RESEND_FROM) {
    return json({ error: "Serviço de e-mail ainda não configurado." }, 503);
  }

  const fields = [
    ["Nome", nome],
    ["E-mail", email],
    ["Telefone / WhatsApp", clean(data.telefone, 80) || "Não informado"],
    ["Assunto", assunto],
    ["Organização ou igreja", clean(data.organizacao, 180) || "Não informada"],
    ["Tipo de convite", clean(data.tipo, 120) || "Não informado"],
    ["Data prevista", clean(data.data, 40) || "Não informada"],
    ["Cidade e local", clean(data.local, 220) || "Não informado"]
  ];
  const rows = fields.map(([label, value]) => `<tr><th style="padding:8px 18px 8px 0;text-align:left;vertical-align:top">${html(label)}</th><td style="padding:8px 0">${html(value)}</td></tr>`).join("");

  const resend = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      authorization: `Bearer ${context.env.RESEND_API_KEY}`,
      "content-type": "application/json"
    },
    body: JSON.stringify({
      from: context.env.RESEND_FROM,
      to: [context.env.CONTACT_TO || RECIPIENT],
      reply_to: email,
      subject: `[Site Luiz Arcanjo] ${assunto}`,
      html: `<div style="font-family:Arial,sans-serif;color:#202d3a;line-height:1.55"><h1 style="font-size:24px">Nova mensagem pelo site</h1><table style="border-collapse:collapse">${rows}</table><h2 style="margin-top:28px;font-size:18px">Mensagem</h2><p>${html(mensagem)}</p></div>`,
      text: `${fields.map(([label, value]) => `${label}: ${value}`).join("\n")}\n\nMensagem:\n${mensagem}`
    })
  });

  const result = await resend.json().catch(() => ({}));
  if (!resend.ok) {
    console.error("Resend contact error", resend.status, result && result.message);
    return json({ error: "Não foi possível enviar a mensagem." }, 502);
  }
  return json({ ok: true, id: result.id });
}
