import { SetStateAction, Dispatch } from "react";

type BundleContentProps = {
  showExpanded: boolean;
  setExpanded: Dispatch<SetStateAction<boolean>>;
  open: () => void;
};

export default BundleContentProps;
