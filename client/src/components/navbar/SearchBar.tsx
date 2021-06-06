import styled from "styled-components";

const FlexRow = styled.div`
  display: flex;
  align-items: center;
  height: inherit;
`;

const Search = styled.input.attrs({
  placeholder: "Search Something....",
})`
  background-color: #7d828a;
  border-color: #494f5c;
  color: #16181d;
  width: 20em;
  height: inherit;
  padding: 0.05em;
  box-sizing: initial;
  font-size: large;
  border-radius: 4px 0px 0px 4px;
  border-width: 0em;
  border-right: none;
  ::placeholder,
  ::-webkit-input-placeholder {
    color: #494f5c;
  }
`;

const SearchBarButton = styled.button.attrs({
  children: "GO!",
})`
  background-color: #7d828a;
  height: inherit;
  padding: 0.05em;
  font-size: large;
  box-sizing: initial;
  border-radius: 0px 4px 4px 0px;
  border-left: none !important;
  border-width: 0em;
  &:hover {
    background-color: #696d747f;
    cursor: pointer;
    padding-top: 0.2em;
    padding-bottom: 0.2em;
  }
  &:active {
    background-color: #696d74;
  }
`;

const SearchBarRoot = styled.div`
  margin-left: 5em;
  height: 2.5em;
`;

const SearchBar = (): JSX.Element => (
  <SearchBarRoot>
    <FlexRow>
      <Search />
      <SearchBarButton />
    </FlexRow>
  </SearchBarRoot>
);

export default SearchBar;
