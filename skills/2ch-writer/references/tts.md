# TTS Conversion Table

This is the closed set of allowed changes between a thread post and the converted script.
Everything outside it stays verbatim (see invariant 11). Every rule keeps the **meaning**
a listener needs and drops only what a listener cannot hear. Spoken forms render in the
request's language per that language's counting and reading convention.

| In the thread | In the script | Why |
|---|---|---|
| Time of day | Spoken form in request language | digits identify a value; they are not speakable, the value is. |
| Dates | Spoken form in request language | same. |
| Measures, money, percentages, ratios | Spoken form in the language's standard reading | same. |
| Post number line, timestamp+ID line | Dropped | metadata; the script's segment labels and heading carry what a listener must know. |
| Post IDs | Never rendered, never spoken — not as label, not in content | random strings identify a row on screen; read aloud they are noise, and the 글쓴이/익명/name roles already replace them (see invariant 12). |
| Anchor substrings in bodies | Dropped — bodies contain zero anchors per invariant 2; when a post's meaning depends on a reference, speak the content it points to in the post's own words | an anchor is a pointer, not speech; the thread's writing rule already makes meaning travel in words and forbids anchors in bodies. |
| Emoticons, emoji | Spoken equivalent; dropped when it has none | sound for sound, or nothing. |
| Letter repetition | Sound equivalent in request language | it is laughter, not a letter string. |
| Markup: bold, italics, strikethrough, HTML tags | Unwrapped; the words stay | styling is not speech; emphasis that carries meaning lives in the words. |
| Quote marks | Dropped; the quoted words stay | marks are formatting; the pause around the quoted line comes from its terminal mark and the spacing constant. |
| Quoted block of another post | Spoken with an explicit frame the request language uses to mark quotation, when the two-newline pause alone would blur whose words they are | a whole quoted post has a voice, not just a color; the frame preserves ownership. |
| Kanji/foreign-script proper nouns that are thread handles | Spoken per the request language's standard reading of that name | the handle is the thread's own proper noun (invariant 7); spelling it out letter-by-letter is not speaking the name. |
| Numbers inside spoken idioms | Spoken form | same rule as measures: value must be heard. |
