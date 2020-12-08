(ns notebook.utils.tree)

(defn tree [data]
  (map (fn [[k vs]] (cons k (tree (keep next vs))))
       (group-by first data)))
