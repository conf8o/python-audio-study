(ns notebook.join-md
  (:require [notebook.utils.path :as path]
            [clojure.string :as string]))

(defn run []
  (spit (str path/base "/index.md")
        (string/join 
         "\n---\n\n"
         (map #(slurp (str path/base %))
              (list
               "/../README.md"
               "/md_link_tree.md"
               "/picked_code_py.md")))))
