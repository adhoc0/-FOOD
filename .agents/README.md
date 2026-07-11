# AI Agent Workspace

## Amaç

Bu klasör, FOOD projesinde kullanılan tüm yapay zekâ ajanlarının ortak çalışma alanıdır.

Bu klasör;

- Kod üretim standartlarını
- Prompt şablonlarını
- Uzmanlık (Skill) bilgilerini
- Referans dokümanlarını
- Yardımcı scriptleri

tek merkezden yönetmek amacıyla oluşturulmuştur.

---

# Klasör Yapısı

.agents/

├── prompts/

├── skills/

---

# Prompts

Prompts klasörü belirli görevler için hazırlanmış standart istemleri içerir.

Örnekler

- Kod inceleme
- Refactor
- Migration
- Performans analizi
- Güvenlik incelemesi
- SEO kontrolü

Prompts doğrudan kod içermez.

Yalnızca AI'ın görevi nasıl yerine getireceğini tanımlar.

---

# Skills

Skills klasörü belirli teknolojiler hakkında uzmanlık bilgisi içerir.

Her Skill aşağıdaki yapıya sahiptir.

SKILL.md

Teknoloji kuralları

references/

Referans dokümanları

scripts/

Yardımcı scriptler

---

# Çalışma Sırası

Bir AI ajanı aşağıdaki sırayla hareket etmelidir.

1. AGENTS.md

2. docs/

3. .agents/skills/

4. .agents/prompts/

5. Proje kodu

---

# Kurallar

- Kurallar birbirini tekrar etmemelidir.
- Her bilgi yalnızca ilgili Skill içinde bulunmalıdır.
- Kod üretmeden önce mevcut yapı analiz edilmelidir.
- Proje mimarisi bozulmamalıdır.
- Gereksiz dosya oluşturulmamalıdır.

---

# Güncelleme

Yeni teknoloji eklendiğinde yeni Skill oluşturulmalıdır.

Mevcut Skill değiştirilirken geriye dönük uyumluluk korunmalıdır.

---

# Hedef

Bu yapı;

- Claude Code
- Codex
- Gemini CLI
- Cursor
- VS Code Agent
- OpenAI Agents

tarafından ortak kullanılabilecek şekilde tasarlanmıştır.