import styled from "styled-components";
import { urlFor } from "../util";

const FooterLogo = styled.img.attrs({
  src: urlFor("footerLogo.png"),
})`
  height: 2.5em;
  padding: 1.25em;
  box-sizing: initial;
`;

const FooterRoot = styled.div`
  height: 20%;
  width: inherit;
  position: fixed;
  bottom: 0;
  background-color: #2f333d;
  position: absolute;
`;

const Footer = (): JSX.Element => (
  <FooterRoot>
    <FooterLogo />
  </FooterRoot>
);

export default Footer;
