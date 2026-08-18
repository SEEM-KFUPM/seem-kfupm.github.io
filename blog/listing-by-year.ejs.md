<div class="quarto-listing quarto-listing-default blog-listing-by-year">

<%
let currentYear;

for (const item of items) {
  const yearMatch = String(item.date).match(/\b\d{4}\b/);
  const year = yearMatch ? yearMatch[0] : "Undated";

  if (year !== currentYear) {
    if (currentYear !== undefined) {
%>
</div>
<%
    }
    currentYear = year;
%>
<h2 class="blog-year"><%= year %></h2>
<div class="list">
<%
  }
%>
<article class="quarto-post blog-listing-item" <%= metadataAttrs(item) %>>
<% if (item.image) { %>
<a class="blog-listing-image" href="<%- item.path %>" aria-label="Read <%= item.title %>">
<img src="<%- item.image %>" alt="<%= item['image-alt'] || '' %>">
</a>
<% } %>
<div class="blog-listing-content">
<div class="body">
<h3 class="no-anchor listing-title"><a href="<%- item.path %>" class="no-external"><%= item.title %></a></h3>
<div class="listing-description"><%= item.description %></div>
</div>
<div class="metadata">
<div class="listing-date"><%= item.date %></div>
<div class="listing-author"><%= item.author %></div>
</div>
</div>
</article>
<%
}

if (currentYear !== undefined) {
%>
</div>
<%
}
%>

</div>
