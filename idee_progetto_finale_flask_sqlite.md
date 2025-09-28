# Idee per Progetto Finale — Flask + Jinja + Form + SQLite (no ORM)

Di seguito 18 idee pronte, tutte compatibili con le competenze del corso (Flask base, template Jinja, form GET/POST, flash+PRG, statici, SQLite con `sqlite3`). Per ogni idea trovi: *pitch*, *core*, *tabelle* e *extra opzionali*.

---

## 1) Mini‑Biblioteca con Prestiti
- **Pitch:** gestire libri e prestiti agli studenti (presa/reso).
- **Core:** CRUD libri; CRUD studenti; registra **prestito** e **reso**; lista “in prestito”.
- **DB (tabelle):** `books(id,title,author,available)` • `students(id,name)` • `loans(id,book_id,student_id,loan_date,return_date)`.
- **Extra:** CSV prestiti; filtro “scaduti”; pagina ricevuta prestito stampabile.

## 2) Registro Consegne Compiti
- **Pitch:** chi ha consegnato quale compito e quando.
- **Core:** CRUD studenti; CRUD compiti; marca **consegnato/non**; note docente.
- **DB:** `students(id,name)` • `assignments(id,title,due_date)` • `submissions(id,student_id,assignment_id,delivered,notes,ts)`.
- **Extra:** CSV per compito; contatori; pagina profilo studente con storico.

## 3) Spese di Classe (entrate/uscite + report)
- **Pitch:** micro‑contabilità per una classe.
- **Core:** voci con `title, amount, type(entrata/uscita), category`; riepilogo **totale** e **per categoria**.
- **DB:** `entries(id,title,amount,type,category,ts)`.
- **Extra:** CSV; range date; “chiusura mese” con pagina stampabile.

## 4) Planner Eventi + Iscrizioni
- **Pitch:** crea eventi e raccogli iscrizioni.
- **Core:** CRUD eventi; iscrizione (nome+email); capienza massima; stato aperto/chiuso.
- **DB:** `events(id,title,date,max_slots,open)` • `registrations(id,event_id,name,email,ts)`.
- **Extra:** waitlist; CSV iscritti; posti rimanenti.

## 5) Ricettario / Meal Planner
- **Pitch:** salva ricette e pianifica i pasti della settimana.
- **Core:** CRUD ricette (titolo, ingredienti, testo); calendario settimanale (pranzo/cena).
- **DB:** `recipes(id,title,ingredients,body)` • `plan(id,date,slot,recipe_id)`.
- **Extra:** lista ingredienti settimanale; duplicazione piano.

## 6) Mini CRM Contatti + Note
- **Pitch:** rubrica con note cronologiche per contatto.
- **Core:** CRUD contatti; aggiungi **note** collegate; “preferito”.
- **DB:** `contacts(id,name,email,phone,star)` • `notes(id,contact_id,body,ts)`.
- **Extra:** CSV contatti; ricerca per nome/email; badge numero note.

## 7) Magazzino / Inventario
- **Pitch:** traccia giacenze e movimenti.
- **Core:** CRUD prodotti; movimenti **carico/scarico** che aggiornano quantità.
- **DB:** `items(id,name,sku,qty)` • `moves(id,item_id,delta,ts,note)`.
- **Extra:** report giacenze; CSV movimenti.

## 8) Kanban Semplice (To‑Do → Doing → Done)
- **Pitch:** bacheca attività a 3 colonne.
- **Core:** task con titolo + colonna; sposta tra colonne; edit/delete.
- **DB:** `tasks(id,title,column,created_at)`.
- **Extra:** ordinamento per data; CSV.

## 9) Issue Tracker per la Classe
- **Pitch:** traccia problemi/bug e priorità.
- **Core:** ticket con **stato** (aperto/chiuso) e **priorità** (basso/medio/alto).
- **DB:** `issues(id,title,body,status,priority,created_at)`.
- **Extra:** filtro via querystring; CSV; counter aperti/chiusi.

## 10) Sondaggi & Voti
- **Pitch:** crea sondaggi con opzioni e raccogli voti.
- **Core:** CRUD sondaggi e opzioni; registra voto (una scelta per studente/nome).
- **DB:** `polls(id,question)` • `options(id,poll_id,text)` • `votes(id,poll_id,option_id,student_name)`.
- **Extra:** risultati aggregati; CSV voti.

## 11) URL Shortener “da aula”
- **Pitch:** link corti per materiali/compiti.
- **Core:** mappa `slug → url`, redirect e conteggio click.
- **DB:** `links(id,slug,url,clicks,created_at)`.
- **Extra:** CSV; pagina top link.

## 12) Habit Tracker
- **Pitch:** traccia abitudini giornaliere.
- **Core:** CRUD abitudini; **check** giornalieri (done sì/no).
- **DB:** `habits(id,title)` • `checks(id,habit_id,date,done)`.
- **Extra:** streak/contatori; CSV.

## 13) Prenotazioni Aula/Attrezzatura
- **Pitch:** prenota risorse scolastiche.
- **Core:** CRUD risorse; prenotazioni con orario e nominativo; prevenzione sovrapposizioni semplici.
- **DB:** `resources(id,name)` • `bookings(id,resource_id,who,start,end)`.
- **Extra:** CSV; segnalazione conflitti.

## 14) Diario di Lettura
- **Pitch:** log di lettura per libro.
- **Core:** libri + **log** (data, pagine, note); stato letto/non letto.
- **DB:** `books(id,title,author,read)` • `reads(id,book_id,date,pages,note)`.
- **Extra:** tot pagine/mese; CSV.

## 15) Catalogo Corsi & Iscrizioni
- **Pitch:** offre corsi e raccoglie iscrizioni.
- **Core:** CRUD corsi (titolo, docente, posti); iscrizioni nome/email; posti rimanenti.
- **DB:** `courses(id,title,teacher,max_slots)` • `enrollments(id,course_id,name,email,ts)`.
- **Extra:** chiusura corso se pieno; CSV iscritti.

## 16) Blog Minimale + Commenti
- **Pitch:** post semplici con commenti.
- **Core:** CRUD post; aggiunta commenti (autore+testo).
- **DB:** `posts(id,title,body,created_at)` • `comments(id,post_id,author,body,created_at)`.
- **Extra:** publish/unpublish (flag); CSV post.

## 17) FAQ / Knowledge Base
- **Pitch:** domande/risposte organizzate per categoria.
- **Core:** CRUD categorie; CRUD FAQ (domanda/risposta); flag “in evidenza”.
- **DB:** `categories(id,name)` • `faqs(id,category_id,question,answer,featured)`.
- **Extra:** ricerca via querystring; CSV.

## 18) Piano Lezioni & Registro Argomenti
- **Pitch:** pianifica lezioni e traccia argomenti svolti.
- **Core:** CRUD lezioni con data/classe; argomento e materiali (testo/URL).
- **DB:** `lessons(id,date,classroom,topic,materials)`.
- **Extra:** riepilogo per classe/mese; CSV.

---

### Consigli per la consegna
- **Struttura:** `app.py`, `templates/`, `static/`, `README.md`, (opz. `schema.sql`).
- **README:** pitch, feature core/extra, schema tabelle, istruzioni avvio, 3–4 screenshot.
- **Valutazione suggerita:** funzionalità (40%), qualità codice (20%), UX/PRG (15%), validazioni (15%), doc (10%).

Buon lavoro! 💪
