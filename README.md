# AMAP Contract Generation

Collection of scripts responsible for the generation of all contracts, forms and templates for the Croix luizet AMAP.

This solution aims at replacing previous process of writing contracts. It's based on nextcloud forms and odt files.

## Glossary
**Shipment dates**: Delivery dates, can vary depending on the **contract type**

**Products**: Products that are sold by the productor, depends on **contract type**

**Basket**: AMAP basket defined by **products** and **shipment dates**

**Contract season**: Season during which the contract is in effect (Hiver-2025, Printemps-2026...)

**Contract type**: Type of the contract (Oeuf, Porc-Agneau, Legumineuses...)

**Contract form** : Contract for members, defined by a **contract season** and a **contract type**

**Contract template**: Cotnract template linked to a **contract form**

**Referer form**: Form for referer, this form allow referer to generate **contract form** and **contract template** for their AMAP Basket

## All contract generation
Generate all contracts based on new answers in *contract forms*.

```mermaid
---
title: All contract generation workflow
---
graph LR;
    Start((Start))-->GetAllContractForms;
    GetAllContractForms(Get all contract forms)-->ForEachContract;
    ForEachContract(ForEach contract)-->GetFormSubmissions;
    GetFormSubmissions(Get form contract submissions)-->FormatSubmissions;
    FormatSubmissions(Format submissions)-->ForEachSubmission;
    ForEachSubmission(ForEach submission)-->GenerateOneContract;
    GenerateOneContract(Generate one contract)-->SubmissionRemaining{Submission remaining ?};
    SubmissionRemaining--Yes-->ForEachSubmission
    SubmissionRemaining--Noo-->ContractRemaining
    ContractRemaining{Contract remaining ?}--Yes-->ForEachContract
    ContractRemaining--Noo-->Stop((Stop));
```

## One contract generation
Generate a contract based on a specific answer in *contract form*.

```mermaid
---
title: One contract generation workflow
---
graph LR;
    Start((Start))-->GetTemplateName(Get contract template name);
    GetTemplateName-->FormatProducts(Format product informations);
    FormatProducts-->GetTemplate(Get contract Template);
    GetTemplate-->FillInformations(Fill informations);
    FillInformations-->CalculateTotals(Calculate total price);
    CalculateTotals-->CreateFolders(Create Folder on Nextcloud);
    CreateFolders-->ConvertOdt(Convert Odt to Pdf);
    CreateFolders-->UploadOdt(Upload Odt on Nextcloud);
    ConvertOdt-->UploadPdf(Upload Pdf on Nextcloud);
    ConvertOdt-->Sendemail(Send Email to member);
    UploadOdt-->Stop((Stop));
    Sendemail-->Stop((Stop));
    UploadPdf-->Stop((Stop));
```

## All form contract generation
Generate all form and templates based on new answers from *referer form*.

```mermaid
---
title: All form contract generation workflow
---
graph LR;
    Start((Start))-->GetAllRefererForm(Get all referer forms);
    GetAllRefererForm-->ForEachRefererForm;
    ForEachRefererForm(ForEach referer form)-->GetRefererSubmission(Get referer submission);
    GetRefererSubmission-->GenerateOneFormTemplateContract(Generate one form / template contract pair);
    GenerateOneFormTemplateContract-->RefererFormRemaining{Referer form remaining ?};
    RefererFormRemaining--Yes-->ForEachRefererForm;
    RefererFormRemaining--Noo-->Stop((Stop))
```

## One form contract generation
Generate a form and template based on a specifi answer from *referer form*.
```mermaid
---
title: One form contract generation workflow
---
graph LR;
    Start((Start))-->FormatInput(Format input);
    FormatInput-->NextcloudWebdavGet(Get contract base template);
    NextcloudWebdavGet-->FillInformation(Fill contract base informations);
    FillInformation-->CreateContractTemplate(Create contract template);
    FormatInput-->GenerateNextcloudForm(Generate Nextcloud form);
    GenerateNextcloudForm-->ShareForm(Share Nextcloud form to referer);
    ShareForm-->CreateMemberLink(Create share link for members);
    CreateContractTemplate-->CreateProductsShipmentsFormTemplate(Create products and shipment template for nextcloud forms fill);
    CreateProductsShipmentsFormTemplate-->WebDavUploadTemplate(Webdav upload files);
    CreateContractTemplate-->CreateProductsShipmentTemplate(Create products and shipment template for manual fill)
    CreateProductsShipmentTemplate-->WebDavUploadTemplate
    WebDavUploadTemplate-->ShareFiles(Share files with referer)
    ShareFiles-->NotifyReferer(Notify referer by mail)
    CreateMemberLink-->Stop((Stop))
    NotifyReferer-->Stop((Stop))
    
```