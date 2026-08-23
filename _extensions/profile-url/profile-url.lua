local function join_path(...)
  local separator = package.config:sub(1, 1)
  return table.concat({ ... }, separator)
end

local function file_exists(path)
  local handle = io.open(path, "r")
  if handle == nil then
    return false
  end

  handle:close()
  return true
end

local function resolve_profile_url(slug)
  if not slug:match("^[a-z0-9][a-z0-9-]*$") then
    error("profile-url: invalid profile slug '" .. slug .. "'")
  end

  local project_directory = quarto.project.directory
  if project_directory == nil then
    error("profile-url: this shortcode must be rendered inside a Quarto project")
  end

  local profiles_directory = join_path(project_directory, "people", "profiles")
  local matches = {}

  for _, group in ipairs(pandoc.system.list_directory(profiles_directory)) do
    local profile = join_path(profiles_directory, group, slug .. ".qmd")
    if file_exists(profile) then
      table.insert(matches, group)
    end
  end

  table.sort(matches)

  if #matches == 0 then
    error(
      "profile-url: no profile found for slug '"
        .. slug
        .. "' below people/profiles/*/"
    )
  end

  if #matches > 1 then
    error(
      "profile-url: duplicate profile slug '"
        .. slug
        .. "' found in: "
        .. table.concat(matches, ", ")
    )
  end

  return "/people/profiles/" .. matches[1] .. "/" .. slug .. ".html"
end

return {
  ["profile-url"] = function(args)
    if args[1] == nil then
      error("profile-url: expected a profile slug")
    end

    local slug = pandoc.utils.stringify(args[1])
    return pandoc.Str(resolve_profile_url(slug))
  end,
}
