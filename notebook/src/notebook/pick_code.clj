(ns notebook.pick-code
  (:require [clojure.string :as string]
            [notebook.utils.path :as path]))

(def py-source
  (->> (path/files ".." "py")
       (filter #(not (re-find #"__init__" (.toString %))))
       sort
       vec))

(def extension "py")

(def source-div-format
  (str
   "%s\n```" extension "\n"
   "%s\n```\n"))

(defn- source-part [source]
  (string/join "\n"
   (for [file source]
     (format source-div-format
             (.getName file)
             (slurp file)))))

(defn run []
  (spit (str path/base "/picked_code_" extension ".md")
        (source-part py-source)))
