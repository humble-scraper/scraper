import styled from "styled-components";

const SectionTitle = styled.div`
    font-family: 'Sofia Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    color: white;
    font-size: 1.17em;
    font-weight: bold;
    margin: 1em;
}
`;

const ContentRoot = styled.div`
  display: block;
`;

const Content = (): JSX.Element => (
  <ContentRoot>
    <SectionTitle>The Ultimate Web Scraping experience!</SectionTitle>
    <SectionTitle>Featured</SectionTitle>
    <SectionTitle>Previously Scrolled</SectionTitle>
    <SectionTitle>Saved</SectionTitle>
  </ContentRoot>
);

export default Content;
