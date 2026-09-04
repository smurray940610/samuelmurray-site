module.exports = function (eleventyConfig) {
  // Copy static assets straight through to the built site.
  eleventyConfig.addPassthroughCopy({ "src/css": "css" });
  eleventyConfig.addPassthroughCopy({ "src/assets": "assets" });
  eleventyConfig.addPassthroughCopy({ "src/admin": "admin" });

  // Friendly date filter for posts (e.g. "June 2026")
  eleventyConfig.addFilter("monthYear", (d) => {
    const date = new Date(d);
    return date.toLocaleDateString("en-US", { month: "long", year: "numeric" });
  });

  // Short year for publication lists (e.g. "'24")
  eleventyConfig.addFilter("shortYear", (y) => "'" + String(y).slice(-2));

  // Zero-pad a number to 2 digits (e.g. 1 -> "01"); used for project numbering.
  eleventyConfig.addFilter("pad2", (n) => String(n).padStart(2, "0"));

  // Filter papers by area + (optionally) exclude reviews. Reliable replacement
  // for Nunjucks selectattr("areas","includes",...), which is flaky on arrays.
  eleventyConfig.addFilter("byArea", (papers, area, includeReviews) => {
    return (papers || [])
      .filter((p) => {
        const inArea = Array.isArray(p.areas) && p.areas.indexOf(area) !== -1;
        const isReview = p.kind === "review";
        if (!inArea) return false;
        if (!includeReviews && isReview) return false;
        return true;
      })
      .sort((a, b) => (b.year || 0) - (a.year || 0));
  });

  // Just the reviews (any area), for the dedicated reviews section.
  eleventyConfig.addFilter("onlyReviews", (papers, area) => {
    return (papers || []).filter(
      (p) => p.kind === "review" && (!area || (Array.isArray(p.areas) && p.areas.indexOf(area) !== -1))
    );
  });

  // Posts collection
  eleventyConfig.addCollection("posts", (api) =>
    api.getFilteredByGlob("src/posts/*.md").reverse()
  );

  return {
    dir: {
      input: "src",
      includes: "_includes",
      data: "_data",
      output: "_site",
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    templateFormats: ["njk", "md", "html"],
  };
};
