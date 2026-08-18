local function alt_text(meta)
  if meta["image-alt"] then
    return pandoc.Plain(meta["image-alt"]).content
  end

  return pandoc.Inlines({})
end

function Pandoc(doc)
  if not doc.meta.image then
    return doc
  end

  local image = pandoc.Image(
    alt_text(doc.meta),
    pandoc.utils.stringify(doc.meta.image)
  )
  local hero = pandoc.Div(
    { pandoc.Para({ image }) },
    pandoc.Attr("", { "blog-post-hero" })
  )

  table.insert(doc.blocks, 1, hero)
  return doc
end
