"use client";
import { Clipboard } from "lucide-react";
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip";
import toast from "react-hot-toast";

// eslint-disable-next-line react/prop-types
const CopyBtn = ({ text }) => {
  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text).then(() => {
    //   alert("Copied to clipboard");
      toast.success("Copied to clipboard")
    });
  };

  return (
    <TooltipProvider>
      <Tooltip>
        <TooltipTrigger asChild>
          <button
            onClick={() => copyToClipboard(text)}
            className="text-slate-50 absolute p-2 right-0 top-0"
          >
            <Clipboard />
          </button>
        </TooltipTrigger>
        <TooltipContent>
          <p>Copy code</p>
        </TooltipContent>
      </Tooltip>
    </TooltipProvider>
  );
};

export default CopyBtn;
