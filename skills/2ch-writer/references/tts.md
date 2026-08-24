# TTS Conversion Table

This is the closed set of allowed changes between a thread post and the converted script.
Everything outside it stays verbatim (see invariant 11). Every rule keeps the **meaning**
a listener needs and drops only what a listener cannot hear. Spoken forms render in the
request's language per that language's counting and reading convention.

| In the thread | In the script | Why |
|---|---|---|
| Time of day, e.g. `12:00:31`, `3시 33분` | Spoken form, e.g. `열두 시 영 분 삼십일 초` | digits identify a value; they are not speakable, the value is. |
| Dates, e.g. `8월 14일`, `2026/08/17` | Spoken form, e.g. `팔월 십사일` | same. |
| Measures, money, percentages, ratios | Spoken form in the language's standard reading | same. |
| Post number line (`12 ：`), timestamp+ID line | Dropped | metadata; the script's segment labels and heading carry what a listener must know. |
| Post IDs (`ID:qXr7mT2z`) | Never rendered, never spoken — not as label, not in content | random strings identify a row on screen; read aloud they are noise, and the 글쓴이/익명/name roles already replace them (see invariant 12). |
| `>>n` anchor | Dropped; when a post's meaning depends on the reference, speak the content it points to in the post's own words | an anchor is a pointer, not speech; the thread's writing rule already makes meaning travel in words. |
| Emoticons, emoji | Spoken equivalent; dropped when it has none | sound for sound, or nothing. |
| Letter repetition (`ㅋㅋㅋ`, `www`, `lol`) | Sound equivalent, e.g. `크크`, `하하` | it is laughter, not a letter string. |
| Markup: bold, italics, strikethrough, HTML tags | Unwrapped; the words stay | styling is not speech; emphasis that carries meaning lives in the words. |
| Quote marks (`"…"`, `「…」`) | Dropped; the quoted words stay | marks are formatting; the pause around the quoted line comes from its terminal mark and the spacing constant. |
| Quoted block of another post | Spoken with an explicit frame the request language uses to mark quotation, e.g. "인용: … 인용 끝", when the two-newline pause alone would blur whose words they are | a whole quoted post has a voice, not just a color; the frame preserves ownership. |
| Karakuri-style kanji/foreign-script proper nouns (`悪魔情報`) | Spoken per the request language's standard reading of that name | the handle is the thread's own proper noun (invariant 7); spelling it out letter-by-letter is not speaking the name. |
| Numbers inside spoken idioms (`1위`, `3주차`, `0회`) | Spoken form (`일 위`, `삼 주차`, `영 회`) | same rule as measures: value must be heard. |
