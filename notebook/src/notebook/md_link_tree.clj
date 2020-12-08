(ns notebook.md-link-tree
  (:require [clojure.string :as string]
            [notebook.utils.path :as path]
            [notebook.utils.tree :as tree]))

(def htmls
  (vec (path/files path/base "html")))

(def html-mapping
  (->> htmls
       (map #(hash-map (.getName %) (string/replace (.toString %) path/base-re ".")))
       (reduce conj {})))

(defn- add-link-to-html [html]
  (if (path/has-extension? html "html")
    (str "[" html "]" "(" (html-mapping html) ")")
    html))

(defn- indented [s i]
  (str (string/join "" (repeat i " ")) s))

(defn- md-link-tree [tree indent]
  (reduce
   (fn [md-list branch]
       (str md-list
            (indented (str "* " (add-link-to-html (first branch))) indent) "\n"
            (md-link-tree (next branch) (+ indent 4))))
   "" 
   tree))

(def paths
  (->> htmls
       (map (comp vec path/path-seq #(.toPath %)))
       sort
       vec))

(defn run []
  (let [tree (-> (tree/tree paths) first rest)]
    (spit (str path/base "/md_link_tree.md")
          (md-link-tree tree 0))))
