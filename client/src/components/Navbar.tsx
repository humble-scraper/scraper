import styled from "styled-components";
import { urlFor } from "../util";

const FlexRow = styled.div`
  display: flex;
  align-items: center;
  height: inherit;
`;

const ImgLogo = styled.img.attrs({
  src: urlFor("logo.png"),
})`
  height: 2.5em;
  padding: 1.25em;
  box-sizing: initial;
`;

const Search = styled.input.attrs({
  placeholder: "Search Something....",
})`
  background-color: #7d828a;
  color: #16181d;
  width: 20em;
  height: inherit;
  padding: 0.05em;
  box-sizing: initial;
  font-size: large;
  border-radius: 4px 0px 0px 4px;
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
  padding: 0.1em;
  font-size: medium;
  box-sizing: initial;
  border-radius: 0px 4px 4px 0px;

  &:hover {
    background-color: #696d747f;
    cursor: pointer;
    padding: 0.2em;
  }
  &:active {
    background-color: #696d74;
  }
`;

const SearchBarRoot = styled.div`
  margin-left: 5em;
  height: 2em;
  
`;
const SearchBar = () => (
  <SearchBarRoot>
    <FlexRow>
      <Search />
      <SearchBarButton />
    </FlexRow>
  </SearchBarRoot>
);

const NavbarRoot = styled.div`
  &&& {
    background-color: #494f5c !important;
    color: #d8d8da;
    border-bottom: 1px #373c46 solid;
    box-shadow: 1px 2px 3px #00000045;
    height: 5em;
    width: 100%;
    display: "flex";
    justify-content: center;
    align-items: center;
    position: sticky;
  }
`;

const Navbar = (): JSX.Element => (
  <NavbarRoot>
    <FlexRow>
      <ImgLogo />
      <SearchBar />
    </FlexRow>
  </NavbarRoot>
);

export default Navbar;
