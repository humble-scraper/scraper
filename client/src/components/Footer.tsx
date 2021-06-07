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
  height: 15%;
  width: inherit;
  bottom: 0;
  background-color: #2f333d;
  position: absolute;
  display:block;
  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
  font-weight: bold;
  color: white;
`;

const Footer = (): JSX.Element => (
  <FooterRoot>
    <FooterLogo />
    <p>Brought to you by E-Dawg ,Ettienne Barsotti and Lustin Joh</p>
  </FooterRoot>
);

export default Footer;
