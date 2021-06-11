import styled from "styled-components";

const FlexRow = styled.div`
  display: flex;
  align-items: center;
  height: inherit;
`;

const LoginButton = styled.button.attrs({
  children: "Log in",
})`
  color: #aaa2a2;
  width: flex;
  height: inherit;
  background-color: #494f5c;
  font-size: inherit;
  border-radius: 4px 0px 0px 4px;
  border: solid;
  letter-spacing: 0.1em;
  &:hover {
    color: #ccc3c3;
    cursor: pointer;
  }
  &:active {
    color: #f1eaea;
  }
`;
const SignInButton = styled.button.attrs({
  children: "Sign up",
})`
  color: #aaa2a2;
  width: flex;
  height: inherit;
  background-color: #494f5c;
  font-size: inherit;
  border-radius: 0px 4px 4px 0px;
  letter-spacing: 0.1em;
  border: solid;
  &:hover {
    color: #ccc3c3;
    cursor: pointer;
  }
  &:active {
    color: #f1eaea;
  }
`;
const AccountsRoot = styled.div`
  margin-left: 30em;
  height: 3em;
  font-size: large;
`;

const AccountBar = (): JSX.Element => (
  <AccountsRoot>
    <FlexRow>
      <LoginButton />
      <SignInButton />
    </FlexRow>
  </AccountsRoot>
);

export default AccountBar;
