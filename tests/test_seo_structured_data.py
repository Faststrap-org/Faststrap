"""Tests for StructuredData helper class."""

import json

from faststrap.seo import StructuredData


class TestArticleStructuredData:
    """Test Article structured data generation."""

    def test_basic_article(self):
        """Test basic article structured data."""
        result = StructuredData.article(
            headline="Test Article",
            description="Article description",
            image="https://example.com/image.jpg",
            author="John Doe",
            published="2026-02-12T10:00:00Z",
        )

        assert result.tag == "script"
        assert result.attrs.get("type") == "application/ld+json"

        data = json.loads(str(result.children[0]))
        assert data["@context"] == "https://schema.org"
        assert data["@type"] == "Article"
        assert data["headline"] == "Test Article"
        assert data["description"] == "Article description"
        assert data["image"] == "https://example.com/image.jpg"
        assert data["author"]["@type"] == "Person"
        assert data["author"]["name"] == "John Doe"
        assert data["datePublished"] == "2026-02-12T10:00:00Z"

    def test_article_with_modified_date(self):
        """Test article with modified date."""
        result = StructuredData.article(
            headline="Test",
            description="Desc",
            image="img.jpg",
            author="Author",
            published="2026-02-12T10:00:00Z",
            modified="2026-02-12T14:00:00Z",
        )

        data = json.loads(str(result.children[0]))
        assert data["dateModified"] == "2026-02-12T14:00:00Z"

    def test_article_with_extra_properties(self):
        """Test article with additional properties."""
        result = StructuredData.article(
            headline="Test",
            description="Desc",
            image="img.jpg",
            author="Author",
            published="2026-02-12T10:00:00Z",
            wordCount=1500,
            inLanguage="en",
        )

        data = json.loads(str(result.children[0]))
        assert data["wordCount"] == 1500
        assert data["inLanguage"] == "en"


class TestProductStructuredData:
    """Test Product structured data generation."""

    def test_basic_product(self):
        """Test basic product structured data."""
        result = StructuredData.product(
            name="Test Product",
            description="Product description",
            image="https://example.com/product.jpg",
            price="99.99",
            currency="USD",
        )

        assert result.tag == "script"
        data = json.loads(str(result.children[0]))

        assert data["@type"] == "Product"
        assert data["name"] == "Test Product"
        assert data["description"] == "Product description"
        assert data["image"] == "https://example.com/product.jpg"
        assert data["offers"]["@type"] == "Offer"
        assert data["offers"]["price"] == "99.99"
        assert data["offers"]["priceCurrency"] == "USD"
        assert data["offers"]["availability"] == "https://schema.org/InStock"

    def test_product_with_rating(self):
        """Test product with rating and reviews."""
        result = StructuredData.product(
            name="Test Product",
            description="Desc",
            image="img.jpg",
            price="49.99",
            rating=4.5,
            review_count=127,
        )

        data = json.loads(str(result.children[0]))
        assert "aggregateRating" in data
        assert data["aggregateRating"]["@type"] == "AggregateRating"
        assert data["aggregateRating"]["ratingValue"] == 4.5
        assert data["aggregateRating"]["reviewCount"] == 127

    def test_product_out_of_stock(self):
        """Test product with OutOfStock availability."""
        result = StructuredData.product(
            name="Test",
            description="Desc",
            image="img.jpg",
            price="99.99",
            availability="OutOfStock",
        )

        data = json.loads(str(result.children[0]))
        assert data["offers"]["availability"] == "https://schema.org/OutOfStock"

    def test_product_with_extra_properties(self):
        """Test product with additional properties."""
        result = StructuredData.product(
            name="Test",
            description="Desc",
            image="img.jpg",
            price="99.99",
            brand="BrandName",
            sku="SKU123",
        )

        data = json.loads(str(result.children[0]))
        assert data["brand"] == "BrandName"
        assert data["sku"] == "SKU123"


class TestBreadcrumbStructuredData:
    """Test Breadcrumb structured data generation."""

    def test_basic_breadcrumb(self):
        """Test basic breadcrumb structured data."""
        items = [
            ("Home", "https://example.com/"),
            ("Products", "https://example.com/products"),
            ("Laptops", "https://example.com/products/laptops"),
        ]

        result = StructuredData.breadcrumb(items)

        assert result.tag == "script"
        data = json.loads(str(result.children[0]))

        assert data["@type"] == "BreadcrumbList"
        assert len(data["itemListElement"]) == 3

        assert data["itemListElement"][0]["position"] == 1
        assert data["itemListElement"][0]["name"] == "Home"
        assert data["itemListElement"][0]["item"] == "https://example.com/"

        assert data["itemListElement"][2]["position"] == 3
        assert data["itemListElement"][2]["name"] == "Laptops"

    def test_single_breadcrumb(self):
        """Test single breadcrumb item."""
        result = StructuredData.breadcrumb([("Home", "https://example.com/")])

        data = json.loads(str(result.children[0]))
        assert len(data["itemListElement"]) == 1


class TestOrganizationStructuredData:
    """Test Organization structured data generation."""

    def test_basic_organization(self):
        """Test basic organization structured data."""
        result = StructuredData.organization(
            name="Acme Corp",
            url="https://acme.com",
            logo="https://acme.com/logo.png",
        )

        assert result.tag == "script"
        data = json.loads(str(result.children[0]))

        assert data["@type"] == "Organization"
        assert data["name"] == "Acme Corp"
        assert data["url"] == "https://acme.com"
        assert data["logo"] == "https://acme.com/logo.png"

    def test_organization_with_social_links(self):
        """Test organization with social media links."""
        social_links = [
            "https://twitter.com/acmecorp",
            "https://linkedin.com/company/acmecorp",
            "https://facebook.com/acmecorp",
        ]

        result = StructuredData.organization(
            name="Acme Corp",
            url="https://acme.com",
            logo="https://acme.com/logo.png",
            social_links=social_links,
        )

        data = json.loads(str(result.children[0]))
        assert "sameAs" in data
        assert len(data["sameAs"]) == 3
        assert data["sameAs"][0] == "https://twitter.com/acmecorp"

    def test_organization_with_extra_properties(self):
        """Test organization with additional properties."""
        result = StructuredData.organization(
            name="Acme Corp",
            url="https://acme.com",
            logo="https://acme.com/logo.png",
            description="Leading provider of widgets",
            foundingDate="2020-01-01",
        )

        data = json.loads(str(result.children[0]))
        assert data["description"] == "Leading provider of widgets"
        assert data["foundingDate"] == "2020-01-01"


class TestLocalBusinessStructuredData:
    """Test LocalBusiness structured data generation."""

    def test_basic_local_business(self):
        """Test basic local business structured data."""
        address = {
            "street": "123 Main St",
            "city": "Springfield",
            "state": "IL",
            "zip": "62701",
            "country": "US",
        }

        result = StructuredData.local_business(
            name="Joe's Coffee Shop",
            address=address,
            phone="+1-555-123-4567",
        )

        assert result.tag == "script"
        data = json.loads(str(result.children[0]))

        assert data["@type"] == "LocalBusiness"
        assert data["name"] == "Joe's Coffee Shop"
        assert data["telephone"] == "+1-555-123-4567"
        assert data["address"]["@type"] == "PostalAddress"
        assert data["address"]["streetAddress"] == "123 Main St"
        assert data["address"]["addressLocality"] == "Springfield"
        assert data["address"]["addressRegion"] == "IL"
        assert data["address"]["postalCode"] == "62701"
        assert data["address"]["addressCountry"] == "US"

    def test_local_business_with_hours(self):
        """Test local business with opening hours."""
        address = {
            "street": "123 Main St",
            "city": "Springfield",
            "state": "IL",
            "zip": "62701",
            "country": "US",
        }
        hours = {
            "Monday-Friday": "9:00-17:00",
            "Saturday": "10:00-14:00",
        }

        result = StructuredData.local_business(
            name="Business",
            address=address,
            phone="+1-555-123-4567",
            hours=hours,
        )

        data = json.loads(str(result.children[0]))
        assert "openingHoursSpecification" in data
        assert len(data["openingHoursSpecification"]) == 2

        spec1 = data["openingHoursSpecification"][0]
        assert spec1["@type"] == "OpeningHoursSpecification"
        assert spec1["dayOfWeek"] == "Monday-Friday"
        assert spec1["opens"] == "9:00"
        assert spec1["closes"] == "17:00"

    def test_local_business_with_extra_properties(self):
        """Test local business with additional properties."""
        address = {
            "street": "123 Main St",
            "city": "Springfield",
            "state": "IL",
            "zip": "62701",
            "country": "US",
        }

        result = StructuredData.local_business(
            name="Business",
            address=address,
            phone="+1-555-123-4567",
            priceRange="$$",
            servesCuisine="Italian",
        )

        data = json.loads(str(result.children[0]))
        assert data["priceRange"] == "$$"
        assert data["servesCuisine"] == "Italian"
