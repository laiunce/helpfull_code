data_categoricas <- data[12:20]

str(data_categoricas)


#sistema_operativo_mobile
table(data_categoricas$sistema_operativo_mobile)
ggplot(data_categoricas, aes(x=sistema_operativo_mobile, y=..count..)) + geom_bar(aes(fill = sistema_operativo_mobile,label = ..count..), position = "dodge")

#profile_id
table(data_categoricas$profile_id)
ggplot(data_categoricas, aes(x=profile_id, y=..count..)) + geom_bar(aes(fill = profile_id,label = ..count..), position = "dodge")

#provider_id
table(data_categoricas$provider_id)
ggplot(data_categoricas, aes(x=provider_id, y=..count..)) + geom_bar(aes(fill = provider_id,label = ..count..), position = "dodge")

#client_id
table(data_categoricas$client_id)
ggplot(data_categoricas, aes(x=client_id, y=..count..)) + geom_bar(aes(fill = client_id,label = ..count..), position = "dodge")

#has_approved_device
table(data_categoricas$has_approved_device)
ggplot(data_categoricas, aes(x=has_approved_device, y=..count..)) + geom_bar(aes(fill = has_approved_device,label = ..count..), position = "dodge")

#has_approved_payment_document
table(data_categoricas$has_approved_payment_document)
ggplot(data_categoricas, aes(x=has_approved_payment_document, y=..count..)) + geom_bar(aes(fill = has_approved_payment_document,label = ..count..), position = "dodge")

#has_approved_payment_user
table(data_categoricas$has_approved_payment_user)
ggplot(data_categoricas, aes(x=has_approved_payment_user, y=..count..)) + geom_bar(aes(fill = has_approved_payment_user,label = ..count..), position = "dodge")

#has_approved_payment_tc
table(data_categoricas$has_approved_payment_tc)
ggplot(data_categoricas, aes(x=has_approved_payment_tc, y=..count..)) + geom_bar(aes(fill = has_approved_payment_tc,label = ..count..), position = "dodge")


#analizo provider_id por fraude en low

#provider_id

data_categoricas_low <-data.frame(data_categoricas$provider_id[data_categoricas$profile_id  %in% 'LOW'])
colnames(data_categoricas_low) <- c('provider_id')
table(data_categoricas_low$provider_id)
ggplot(data_categoricas_low, aes(x=provider_id, y=..count..)) + geom_bar(aes(fill = provider_id,label = ..count..), position = "dodge")



#####

