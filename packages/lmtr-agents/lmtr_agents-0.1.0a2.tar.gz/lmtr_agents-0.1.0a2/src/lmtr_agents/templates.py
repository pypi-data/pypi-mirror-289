"""Define templates."""

template_tr = """\
You are an expert {to_lang} translator. Your task is to translate \
TEXT into {to_lang}. You translate text into smooth and natural \
{to_lang} while maintaining the meaning in the original text. \
You only provide translated text and nothing else.

{text}"""


# https://huggingface.co/spaces/mikeee/translation-agent-ui/blob/main/src/translation_agent/utils.py
template_ref = """You are an expert linguist specializing in translation from any language to {to_lang}. \
You will be provided with a source text and its initial translation and your goal is to improve the initial translation.

Your task is to carefully read a source text and an initial {to_lang} translation, and then give constructive criticism and helpful suggestions to improve the translation.
The source text and initial translation, delimited by XML tags <SOURCE_TEXT></SOURCE_TEXT> and <INITIAL_TRANSLATION></INITIAL_TRANSLATION>, are as follows:
<SOURCE_TEXT>
{text}
</SOURCE_TEXT>
<INITIAL_TRANSLATION>
{trtext}
</INITIAL_TRANSLATION>
When writing suggestions, pay attention to whether there are ways to improve the translation's \n\
(i) accuracy (by correcting errors of addition, mistranslation, omission, or untranslated text),\n\
(ii) fluency (by applying {to_lang} grammar, spelling and punctuation rules, and ensuring there are no unnecessary repetitions),\n\
(iii) style (by ensuring the translations reflect the style of the source text and takes into account any cultural context),\n\
(iv) terminology (by ensuring terminology use is consistent and reflects the source text domain; and by only ensuring you use equivalent idioms {to_lang}).\n\
Write a list of specific, helpful and constructive suggestions for improving the translation.
Each suggestion should address one specific part of the translation.
Output only the suggestions and nothing else."""

template_imp = """You are an expert linguist, specializing in translation editing from any language to {to_lang}.
Your task is to carefully read, then edit the initial {to_lang} translation and give an edited {to_lang} translation, taking into account a list of expert suggestions and constructive criticisms.
The source text, the initial translation, and the expert linguist suggestions are delimited by XML tags <SOURCE_TEXT></SOURCE_TEXT>, <INITIAL_TRANSLATION></INITIAL_TRANSLATION> and <EXPERT_SUGGESTIONS></EXPERT_SUGGESTIONS> \
as follows:
<SOURCE_TEXT>
{text}
</SOURCE_TEXT>
<INITIAL_TRANSLATION>
{trtext}
</INITIAL_TRANSLATION>
<EXPERT_SUGGESTIONS>
{reflection}
</EXPERT_SUGGESTIONS>
Please take into account the expert suggestions when editing the translation. Edit the translation by ensuring:
(i) accuracy (by correcting errors of addition, mistranslation, omission, or untranslated text),
(ii) fluency (by applying {to_lang} grammar, spelling and punctuation rules and ensuring there are no unnecessary repetitions), \
(iii) style (by ensuring the translations reflect the style of the source text)
(iv) terminology (inappropriate for context, inconsistent use), or
(v) other errors.
Only output edited translation and nothing else.
edited translation: """

template_comb = """\
Given the below two translations delimited by XML tags
<TRANSLATION_1></TRANSLATION_1> and <TRANSLATION_2></TRANSLATION_2> as follows:

<TRANSLATION_1>
{translation1}
</TRANSLATION_1>

<TRANSLATION_2>
{translation2}
</TRANSLATION_2>

Combine and mix the two translations coherently without repeating, taking into accont of both translations. Only output the final combined and mixed translation and nothing else.

Combined translation:
"""

template_comb_imp = """\
Given the below two translations and expert suggestions delimited by XML tags
<TRANSLATION_1></TRANSLATION_1> and <TRANSLATION_2></TRANSLATION_2> <EXPERT_SUGGESTIONS></EXPERT_SUGGESTIONS> as follows:

<TRANSLATION_1>
{translation1}
</TRANSLATION_1>

<TRANSLATION_2>
{translation2}
</TRANSLATION_2>

<EXPERT_SUGGESTIONS>
{reflection}
</EXPERT_SUGGESTIONS>

Combine and mix the two translations coherently without repeating, taking into accont of both translations and EXPERT SUGGESTIONS. Only output the final combined and mixed translation and nothing else.

Final translation:
"""

template_comb_imp1 = """\
Given the below source text, two translations and expert suggestions delimited by XML tags
<SOURCE_TEXT></SOURCE_TEXT>,
<TRANSLATION_1></TRANSLATION_1> and <TRANSLATION_2></TRANSLATION_2> <EXPERT_SUGGESTIONS></EXPERT_SUGGESTIONS> as follows:

<SOURCE_TEXT>
{text}
</SOURCE_TEXT>

<TRANSLATION_1>
{translation1}
</TRANSLATION_1>

<TRANSLATION_2>
{translation2}
</TRANSLATION_2>

<EXPERT_SUGGESTIONS>
{reflection}
</EXPERT_SUGGESTIONS>

Combine and mix the two translations coherently without repeating, taking into accont of both translations and EXPERT SUGGESTIONS. Only output the final combined and mixed translation and nothing else.

Final translation:
"""
