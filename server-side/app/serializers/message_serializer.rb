class MessageSerializer < ActiveModel::Serializer
  attributes :id, :sanitized_text, :image
end
