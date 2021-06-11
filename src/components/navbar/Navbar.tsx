import styled from "styled-components";
import SearchBar from "./SearchBar";
import AccountBar from "./AccountBar";
import { urlFor } from "../../util";

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
      <AccountBar />
    </FlexRow>
  </NavbarRoot>
);

export default Navbar;
