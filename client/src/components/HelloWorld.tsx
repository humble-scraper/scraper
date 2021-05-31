import styled from "styled-components";

const HelloWorld = styled.div.attrs({ children: "Hello World!" })<{
  $someFlag?: boolean;
}>`
  display: flex;
  margin: auto;

  ${({ $someFlag }) => $someFlag && ``}
`;

export default HelloWorld;
export { HelloWorld };
