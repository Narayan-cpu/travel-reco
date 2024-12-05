/* eslint-disable no-unused-vars */
import { useState, useEffect, useRef } from "react";
import PropTypes from "prop-types";
import { useChat } from "ai/react";
import { MessageCircle, X, Send, Github } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";
import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
  CardFooter,
} from "@/components/ui/card";
import axios from "axios";
import tailwindStyles from "../index.css?inline";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { atomDark } from "react-syntax-highlighter/dist/esm/styles/prism";

const Chatbot = ({ apiKey, apiModel }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [generatingAnswer, setGeneratingAnswer] = useState(false);
  const [error, setError] = useState(null);
  const {
    messages,
    input,
    handleInputChange,
    handleSubmit,
    setMessages,
    setInput,
  } = useChat();
  const messagesEndRef = useRef(null);

  const actualApiKey = apiKey;
  const actualApiModel = apiModel;

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(scrollToBottom, [messages]);

  const generateAnswer = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    setGeneratingAnswer(true);
    setError(null);
    const userMessage = { role: "user", content: input };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setInput(""); // Clear the input after sending

    try {
      const response = await axios.post(
        `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${actualApiKey}`,
        { contents: [{ parts: [{ text: input }] }] }
      );
      const answer = response.data.candidates[0].content.parts[0].text;
      const assistantMessage = { role: "assistant", content: answer };
      setMessages((prevMessages) => [...prevMessages, assistantMessage]);
    } catch (error) {
      console.error("Error details:", error);
      let errorMessage = "Sorry - Something went wrong. Please try again!";

      if (error.response) {
        if (error.response.status === 400) {
          errorMessage =
            "Invalid API key. Please check your API key and try again.";
        } else if (error.response.status === 404) {
          errorMessage =
            "Invalid model name. Please check the model name and try again.";
        }
      }

      setError(errorMessage);
      const assistantMessage = { role: "assistant", content: errorMessage };
      setMessages((prevMessages) => [...prevMessages, assistantMessage]);
    } finally {
      setGeneratingAnswer(false);
    }
  };

  return (
    <>
      <style>{tailwindStyles}</style>
      <div className="widget fixed bottom-4 right-4 z-50 md:bottom-8 md:right-8">
        {!isOpen ? (
          <Button
            onClick={() => setIsOpen(true)}
            className="rounded-full w-12 h-12 md:w-14 md:h-14 bg-purple-600 hover:bg-purple-700 transition-all duration-300 shadow-lg hover:shadow-xl"
          >
            <MessageCircle className="h-5 w-5 md:h-6 md:w-6" />
          </Button>
        ) : (
          <Card className="widget w-full max-w-xs sm:max-w-sm md:max-w-md lg:max-w-lg h-[80vh] md:h-[70vh] lg:h-[60vh] shadow-2xl rounded-2xl overflow-hidden transition-all duration-300 flex flex-col">
            <CardHeader className="bg-gradient-to-r from-purple-600 to-indigo-600 text-white p-3 md:p-4 flex-shrink-0">
              <CardTitle className="flex justify-between items-center text-lg md:text-xl">
                AI Assistant
                <Button
                  variant="ghost"
                  size="icon"
                  onClick={() => setIsOpen(false)}
                  className="hover:bg-white/20 rounded-full transition-colors duration-200"
                >
                  <X className="h-4 w-4" />
                </Button>
              </CardTitle>
            </CardHeader>
            <CardContent className="widget p-0 flex-grow overflow-hidden">
              <ScrollArea className="h-full p-3 md:p-4">
                {messages.map((message, index) => (
                  <div
                    key={index}
                    className={`mb-3 md:mb-4 max-w-[80%] ${
                      message.role === "user" ? "ml-auto" : "mr-auto"
                    }`}
                  >
                    <div
                      className={`p-2 md:p-3 rounded-lg ${
                        message.role === "user"
                          ? "bg-purple-100 text-purple-900"
                          : "bg-white text-gray-900 shadow-md"
                      }`}
                    >
                      <ReactMarkdown
                        remarkPlugins={[remarkGfm]}
                        components={{
                          code({ inline, className, children, ...props }) {
                            const match = /language-(\w+)/.exec(
                              className || ""
                            );
                            return !inline && match ? (
                              <SyntaxHighlighter
                                style={atomDark}
                                language={match[1]}
                                PreTag="div"
                                {...props}
                              >
                                {String(children).replace(/\n$/, "")}
                              </SyntaxHighlighter>
                            ) : (
                              <code className={className} {...props}>
                                {children}
                              </code>
                            );
                          },
                          table({ children }) {
                            return (
                              <div className="overflow-x-auto">
                                <table className="table-auto border-collapse border border-gray-300 text-sm">
                                  {children}
                                </table>
                              </div>
                            );
                          },
                          th({ children }) {
                            return (
                              <th className="border border-gray-300 px-2 py-1 md:px-4 md:py-2 bg-gray-100">
                                {children}
                              </th>
                            );
                          },
                          td({ children }) {
                            return (
                              <td className="border border-gray-300 px-2 py-1 md:px-4 md:py-2">
                                {children}
                              </td>
                            );
                          },
                        }}
                        className="prose prose-sm md:prose-base max-w-none break-words"
                      >
                        {message.content}
                      </ReactMarkdown>
                    </div>
                  </div>
                ))}
                <div ref={messagesEndRef} />
              </ScrollArea>
            </CardContent>
            <CardFooter className="widget p-3 md:p-4 border-t bg-gray-50 flex flex-col space-y-2 flex-shrink-0">
              {error && (
                <div className="text-red-500 text-sm mb-2">{error}</div>
              )}
              <form onSubmit={generateAnswer} className="w-full">
                <div className="flex w-full space-x-2">
                  <Input
                    value={input}
                    onChange={handleInputChange}
                    placeholder="Type your message..."
                    className="flex-grow rounded-full border-gray-300 focus:border-purple-500 focus:ring focus:ring-purple-200 transition-all duration-200 text-sm md:text-base"
                  />
                  <Button
                    type="submit"
                    disabled={generatingAnswer}
                    className="rounded-full bg-purple-600 hover:bg-purple-700 transition-colors duration-200"
                  >
                    {generatingAnswer ? (
                      <div className="w-4 h-4 md:w-5 md:h-5 border-t-2 border-white rounded-full animate-spin" />
                    ) : (
                      <Send className="h-4 w-4" />
                    )}
                  </Button>
                </div>
              </form>
              <div className="flex justify-between items-center w-full text-xs text-gray-500">
                <span>Powered by Google Gemini</span>
                <a
                  href="https://github.com/AJAmit17"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center hover:text-purple-600 transition-colors duration-200"
                >
                  <span className="mr-1">Made by Amit</span>
                  <Github className="h-3 w-3" />
                </a>
              </div>
            </CardFooter>
          </Card>
        )}
      </div>
    </>
  );
};

export default Chatbot;
