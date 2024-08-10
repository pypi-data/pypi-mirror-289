# Toolforge I18n

A **work in progress** library for making Wikimedia Toolforge tools written in Python+Flask translatable.

## Features

- Make your tool translatable into dozens,
  potentially hundreds of languages!

- Easy integration with [translatewiki.net][]
  by reusing MediaWiki message file syntax.

- Full support for the [magic words][]
  `{{GENDER:}}` and `{{PLURAL:}}`,
  as well as for hyperlink syntax (`[url text]`)
  and list formatting.

  - Note that there is no support for any other wikitext syntax;
    formatting in messages (e.g. bold passages) should be written in plain HTML,
    if it can’t be left out the message entirely
    (e.g. on a surrounding element in the template).

- By default, support for a MediaWiki-like
  `?uselang=` URL parameter,
  including `?uselang=qqx` to see message keys.

- Correct conversion between MediaWiki language codes
  and HTML language codes / IETF BCP 47 language tags;
  for instance, `?uselang=simple` produces `<html lang="en-simple">`.

- Correct `lang=` and `dir=` in the face of language fallback:
  messages that (due to language fallback) don’t match the surrounding markup
  are automatically wrapped in a `<span>` with the right attributes.
  (Even MediaWiki doesn’t do this!
  Though, admittedly, MediaWiki doesn’t have the luxury of assuming
  that every message can be wrapped in a `<span>` –
  many MediaWiki messages are block elements that would rather need a `<div>`.)

- Includes checks to ensure all translations are safe,
  without unexpected elements (e.g. `<script>`)
  or attributes (e.g. `onclick=`),
  to protect against XSS attacks from translations.
  The tests are automatically registered via a pytest plugin
  and also run at tool initialization time.

## How to use it

The library is still a work in progress, so preferably don’t use it yet :)
but if you’re feeling adventurous, see the documentation (`docs/` folder; link to follow).

## License

BSD-3-Clause

[translatewiki.net]: https://translatewiki.net/
[magic words]: https://www.mediawiki.org/wiki/Special:MyLanguage/Help:Magic_words
[pip-tools]: https://pip-tools.readthedocs.io/en/latest/
