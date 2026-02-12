"""Tests for SEO meta tags component."""

from faststrap.seo import SEO


class TestSEOBasicTags:
    """Test basic SEO meta tags generation."""

    def test_title_tag(self):
        """Test title tag generation."""
        result = SEO(title="Test Page")
        elements = list(result)

        # Should have Title element
        titles = [e for e in elements if e.tag == "title"]
        assert len(titles) == 1
        assert str(titles[0]) == "<title>Test Page</title>"

        # Should have meta title
        meta_titles = [e for e in elements if e.tag == "meta" and e.attrs.get("name") == "title"]
        assert len(meta_titles) == 1

    def test_description_tag(self):
        """Test description meta tag."""
        result = SEO(description="Test description")
        elements = list(result)

        descriptions = [
            e for e in elements if e.tag == "meta" and e.attrs.get("name") == "description"
        ]
        assert len(descriptions) == 1
        assert descriptions[0].attrs.get("content") == "Test description"

    def test_keywords_tag(self):
        """Test keywords meta tag."""
        result = SEO(keywords=["python", "fasthtml", "seo"])
        elements = list(result)

        keywords = [e for e in elements if e.tag == "meta" and e.attrs.get("name") == "keywords"]
        assert len(keywords) == 1
        assert keywords[0].attrs.get("content") == "python, fasthtml, seo"

    def test_robots_tag(self):
        """Test robots meta tag."""
        result = SEO(robots="noindex, nofollow")
        elements = list(result)

        robots = [e for e in elements if e.tag == "meta" and e.attrs.get("name") == "robots"]
        assert len(robots) == 1
        assert robots[0].attrs.get("content") == "noindex, nofollow"

    def test_canonical_url(self):
        """Test canonical URL link tag."""
        result = SEO(canonical="https://example.com/page")
        elements = list(result)

        canonical = [e for e in elements if e.tag == "link" and e.attrs.get("rel") == "canonical"]
        assert len(canonical) == 1
        assert canonical[0].attrs.get("href") == "https://example.com/page"

    def test_canonical_defaults_to_url(self):
        """Test canonical defaults to url parameter."""
        result = SEO(url="https://example.com/page")
        elements = list(result)

        canonical = [e for e in elements if e.tag == "link" and e.attrs.get("rel") == "canonical"]
        assert len(canonical) == 1
        assert canonical[0].attrs.get("href") == "https://example.com/page"


class TestOpenGraphTags:
    """Test Open Graph meta tags."""

    def test_og_basic_tags(self):
        """Test basic Open Graph tags."""
        result = SEO(
            title="OG Test",
            description="OG Description",
            image="https://example.com/image.jpg",
            url="https://example.com/page",
        )
        elements = list(result)

        og_title = [
            e for e in elements if e.tag == "meta" and e.attrs.get("property") == "og:title"
        ]
        assert len(og_title) == 1
        assert og_title[0].attrs.get("content") == "OG Test"

        og_desc = [
            e for e in elements if e.tag == "meta" and e.attrs.get("property") == "og:description"
        ]
        assert len(og_desc) == 1
        assert og_desc[0].attrs.get("content") == "OG Description"

        og_image = [
            e for e in elements if e.tag == "meta" and e.attrs.get("property") == "og:image"
        ]
        assert len(og_image) == 1
        assert og_image[0].attrs.get("content") == "https://example.com/image.jpg"

        og_url = [e for e in elements if e.tag == "meta" and e.attrs.get("property") == "og:url"]
        assert len(og_url) == 1
        assert og_url[0].attrs.get("content") == "https://example.com/page"

    def test_og_type_website(self):
        """Test Open Graph type defaults to website."""
        result = SEO(title="Test")
        elements = list(result)

        og_type = [e for e in elements if e.tag == "meta" and e.attrs.get("property") == "og:type"]
        assert len(og_type) == 1
        assert og_type[0].attrs.get("content") == "website"

    def test_og_type_article(self):
        """Test Open Graph type set to article."""
        result = SEO(title="Test", type="article")
        elements = list(result)

        og_type = [e for e in elements if e.tag == "meta" and e.attrs.get("property") == "og:type"]
        assert len(og_type) == 1
        assert og_type[0].attrs.get("content") == "article"

    def test_og_locale(self):
        """Test Open Graph locale tags."""
        result = SEO(
            title="Test",
            locale="en_US",
            alternate_locales=["es_ES", "fr_FR"],
        )
        elements = list(result)

        og_locale = [
            e for e in elements if e.tag == "meta" and e.attrs.get("property") == "og:locale"
        ]
        assert len(og_locale) == 1
        assert og_locale[0].attrs.get("content") == "en_US"

        og_alt_locales = [
            e
            for e in elements
            if e.tag == "meta" and e.attrs.get("property") == "og:locale:alternate"
        ]
        assert len(og_alt_locales) == 2


class TestArticleTags:
    """Test article-specific meta tags."""

    def test_article_flag_sets_type(self):
        """Test article=True sets og:type to article."""
        result = SEO(title="Test", article=True)
        elements = list(result)

        og_type = [e for e in elements if e.tag == "meta" and e.attrs.get("property") == "og:type"]
        assert len(og_type) == 1
        assert og_type[0].attrs.get("content") == "article"

    def test_article_published_time(self):
        """Test article published time."""
        result = SEO(
            title="Test",
            article=True,
            published_time="2026-02-12T10:00:00Z",
        )
        elements = list(result)

        published = [
            e
            for e in elements
            if e.tag == "meta" and e.attrs.get("property") == "article:published_time"
        ]
        assert len(published) == 1
        assert published[0].attrs.get("content") == "2026-02-12T10:00:00Z"

    def test_article_modified_time(self):
        """Test article modified time."""
        result = SEO(
            title="Test",
            article=True,
            modified_time="2026-02-12T14:00:00Z",
        )
        elements = list(result)

        modified = [
            e
            for e in elements
            if e.tag == "meta" and e.attrs.get("property") == "article:modified_time"
        ]
        assert len(modified) == 1
        assert modified[0].attrs.get("content") == "2026-02-12T14:00:00Z"

    def test_article_author(self):
        """Test article author."""
        result = SEO(title="Test", article=True, author="John Doe")
        elements = list(result)

        author = [
            e for e in elements if e.tag == "meta" and e.attrs.get("property") == "article:author"
        ]
        assert len(author) == 1
        assert author[0].attrs.get("content") == "John Doe"

    def test_article_section(self):
        """Test article section."""
        result = SEO(title="Test", article=True, section="Technology")
        elements = list(result)

        section = [
            e for e in elements if e.tag == "meta" and e.attrs.get("property") == "article:section"
        ]
        assert len(section) == 1
        assert section[0].attrs.get("content") == "Technology"

    def test_article_tags(self):
        """Test article tags."""
        result = SEO(title="Test", article=True, tags=["python", "fasthtml", "seo"])
        elements = list(result)

        tags = [e for e in elements if e.tag == "meta" and e.attrs.get("property") == "article:tag"]
        assert len(tags) == 3


class TestTwitterCardTags:
    """Test Twitter Card meta tags."""

    def test_twitter_basic_tags(self):
        """Test basic Twitter Card tags."""
        result = SEO(
            title="Twitter Test",
            description="Twitter Description",
            image="https://example.com/twitter.jpg",
        )
        elements = list(result)

        tw_card = [e for e in elements if e.tag == "meta" and e.attrs.get("name") == "twitter:card"]
        assert len(tw_card) == 1
        assert tw_card[0].attrs.get("content") == "summary_large_image"

        tw_title = [
            e for e in elements if e.tag == "meta" and e.attrs.get("name") == "twitter:title"
        ]
        assert len(tw_title) == 1
        assert tw_title[0].attrs.get("content") == "Twitter Test"

        tw_desc = [
            e for e in elements if e.tag == "meta" and e.attrs.get("name") == "twitter:description"
        ]
        assert len(tw_desc) == 1
        assert tw_desc[0].attrs.get("content") == "Twitter Description"

        tw_image = [
            e for e in elements if e.tag == "meta" and e.attrs.get("name") == "twitter:image"
        ]
        assert len(tw_image) == 1
        assert tw_image[0].attrs.get("content") == "https://example.com/twitter.jpg"

    def test_twitter_card_type(self):
        """Test Twitter card type."""
        result = SEO(title="Test", twitter_card="summary")
        elements = list(result)

        tw_card = [e for e in elements if e.tag == "meta" and e.attrs.get("name") == "twitter:card"]
        assert len(tw_card) == 1
        assert tw_card[0].attrs.get("content") == "summary"

    def test_twitter_site_handle(self):
        """Test Twitter site handle."""
        result = SEO(title="Test", twitter_site="@mysite")
        elements = list(result)

        tw_site = [e for e in elements if e.tag == "meta" and e.attrs.get("name") == "twitter:site"]
        assert len(tw_site) == 1
        assert tw_site[0].attrs.get("content") == "@mysite"

    def test_twitter_creator_handle(self):
        """Test Twitter creator handle."""
        result = SEO(title="Test", twitter_creator="@johndoe")
        elements = list(result)

        tw_creator = [
            e for e in elements if e.tag == "meta" and e.attrs.get("name") == "twitter:creator"
        ]
        assert len(tw_creator) == 1
        assert tw_creator[0].attrs.get("content") == "@johndoe"


class TestSEOIntegration:
    """Test SEO component integration scenarios."""

    def test_complete_blog_post_seo(self):
        """Test complete blog post SEO setup."""
        result = SEO(
            title="10 Tips for Better Python Code - My Blog",
            description="Learn how to write cleaner, more maintainable Python code",
            keywords=["python", "coding", "best practices"],
            image="https://example.com/python-tips.jpg",
            url="https://example.com/blog/python-tips",
            article=True,
            published_time="2026-02-12T10:00:00Z",
            modified_time="2026-02-12T14:30:00Z",
            author="Jane Smith",
            section="Programming",
            tags=["python", "tutorial"],
            twitter_site="@myblog",
            twitter_creator="@janesmith",
            locale="en_US",
        )

        elements = list(result)

        # Should have all major tag types
        assert any(e.tag == "title" for e in elements)
        assert any(e.tag == "link" and e.attrs.get("rel") == "canonical" for e in elements)
        assert any(e.tag == "meta" and e.attrs.get("property") == "og:title" for e in elements)
        assert any(e.tag == "meta" and e.attrs.get("property") == "og:type" for e in elements)
        assert any(
            e.tag == "meta" and e.attrs.get("property") == "article:published_time"
            for e in elements
        )
        assert any(e.tag == "meta" and e.attrs.get("name") == "twitter:card" for e in elements)

    def test_custom_meta_tags(self):
        """Test custom meta tags via kwargs."""
        result = SEO(
            title="Test",
            custom_tag="custom value",
            another_tag="another value",
        )
        elements = list(result)

        custom = [e for e in elements if e.tag == "meta" and e.attrs.get("name") == "custom-tag"]
        assert len(custom) == 1
        assert custom[0].attrs.get("content") == "custom value"

        another = [e for e in elements if e.tag == "meta" and e.attrs.get("name") == "another-tag"]
        assert len(another) == 1
        assert another[0].attrs.get("content") == "another value"

    def test_minimal_seo(self):
        """Test minimal SEO with just title."""
        result = SEO(title="Minimal Page")
        elements = list(result)

        # Should still have essential tags
        assert any(e.tag == "title" for e in elements)
        assert any(e.tag == "meta" and e.attrs.get("property") == "og:title" for e in elements)
        assert any(e.tag == "meta" and e.attrs.get("name") == "twitter:card" for e in elements)
