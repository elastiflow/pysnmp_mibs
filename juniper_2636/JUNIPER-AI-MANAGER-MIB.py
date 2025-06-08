# SNMP MIB module (JUNIPER-AI-MANAGER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-AI-MANAGER-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:48:42 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(jnxAdvancedInsightMgr,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxAdvancedInsightMgr")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxAIManager = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1)
)
if mibBuilder.loadTexts:
    jnxAIManager.setRevisions(
        ("2007-10-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxAIManagerNotifications_ObjectIdentity = ObjectIdentity
jnxAIManagerNotifications = _JnxAIManagerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0)
)


class _JnxAIMDescr_Type(DisplayString):
    """Custom type jnxAIMDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMDescr_Type.__name__ = "DisplayString"
_JnxAIMDescr_Object = MibScalar
jnxAIMDescr = _JnxAIMDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 1),
    _JnxAIMDescr_Type()
)
jnxAIMDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMDescr.setStatus("current")


class _JnxAIMHostName_Type(DisplayString):
    """Custom type jnxAIMHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMHostName_Type.__name__ = "DisplayString"
_JnxAIMHostName_Object = MibScalar
jnxAIMHostName = _JnxAIMHostName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 2),
    _JnxAIMHostName_Type()
)
jnxAIMHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMHostName.setStatus("current")


class _JnxAIMOrganization_Type(DisplayString):
    """Custom type jnxAIMOrganization based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMOrganization_Type.__name__ = "DisplayString"
_JnxAIMOrganization_Object = MibScalar
jnxAIMOrganization = _JnxAIMOrganization_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 3),
    _JnxAIMOrganization_Type()
)
jnxAIMOrganization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMOrganization.setStatus("current")


class _JnxAIMIncidentHostID_Type(DisplayString):
    """Custom type jnxAIMIncidentHostID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMIncidentHostID_Type.__name__ = "DisplayString"
_JnxAIMIncidentHostID_Object = MibScalar
jnxAIMIncidentHostID = _JnxAIMIncidentHostID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 4),
    _JnxAIMIncidentHostID_Type()
)
jnxAIMIncidentHostID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMIncidentHostID.setStatus("current")


class _JnxAIMCaseID_Type(DisplayString):
    """Custom type jnxAIMCaseID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMCaseID_Type.__name__ = "DisplayString"
_JnxAIMCaseID_Object = MibScalar
jnxAIMCaseID = _JnxAIMCaseID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 5),
    _JnxAIMCaseID_Type()
)
jnxAIMCaseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMCaseID.setStatus("current")


class _JnxAIMIssueDate_Type(DisplayString):
    """Custom type jnxAIMIssueDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMIssueDate_Type.__name__ = "DisplayString"
_JnxAIMIssueDate_Object = MibScalar
jnxAIMIssueDate = _JnxAIMIssueDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 6),
    _JnxAIMIssueDate_Type()
)
jnxAIMIssueDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMIssueDate.setStatus("current")


class _JnxAIMIPAddress_Type(DisplayString):
    """Custom type jnxAIMIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMIPAddress_Type.__name__ = "DisplayString"
_JnxAIMIPAddress_Object = MibScalar
jnxAIMIPAddress = _JnxAIMIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 7),
    _JnxAIMIPAddress_Type()
)
jnxAIMIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMIPAddress.setStatus("current")


class _JnxAIMSerialNumber_Type(DisplayString):
    """Custom type jnxAIMSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMSerialNumber_Type.__name__ = "DisplayString"
_JnxAIMSerialNumber_Object = MibScalar
jnxAIMSerialNumber = _JnxAIMSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 8),
    _JnxAIMSerialNumber_Type()
)
jnxAIMSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMSerialNumber.setStatus("current")


class _JnxAIMPartNumber_Type(DisplayString):
    """Custom type jnxAIMPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMPartNumber_Type.__name__ = "DisplayString"
_JnxAIMPartNumber_Object = MibScalar
jnxAIMPartNumber = _JnxAIMPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 9),
    _JnxAIMPartNumber_Type()
)
jnxAIMPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMPartNumber.setStatus("current")


class _JnxAIMContractAgreementNumber_Type(DisplayString):
    """Custom type jnxAIMContractAgreementNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMContractAgreementNumber_Type.__name__ = "DisplayString"
_JnxAIMContractAgreementNumber_Object = MibScalar
jnxAIMContractAgreementNumber = _JnxAIMContractAgreementNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 10),
    _JnxAIMContractAgreementNumber_Type()
)
jnxAIMContractAgreementNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMContractAgreementNumber.setStatus("current")


class _JnxAIMContractAgreementStatus_Type(DisplayString):
    """Custom type jnxAIMContractAgreementStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMContractAgreementStatus_Type.__name__ = "DisplayString"
_JnxAIMContractAgreementStatus_Object = MibScalar
jnxAIMContractAgreementStatus = _JnxAIMContractAgreementStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 11),
    _JnxAIMContractAgreementStatus_Type()
)
jnxAIMContractAgreementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMContractAgreementStatus.setStatus("current")


class _JnxAIMContractSKU_Type(DisplayString):
    """Custom type jnxAIMContractSKU based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMContractSKU_Type.__name__ = "DisplayString"
_JnxAIMContractSKU_Object = MibScalar
jnxAIMContractSKU = _JnxAIMContractSKU_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 12),
    _JnxAIMContractSKU_Type()
)
jnxAIMContractSKU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMContractSKU.setStatus("current")


class _JnxAIMContractSKUType_Type(DisplayString):
    """Custom type jnxAIMContractSKUType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMContractSKUType_Type.__name__ = "DisplayString"
_JnxAIMContractSKUType_Object = MibScalar
jnxAIMContractSKUType = _JnxAIMContractSKUType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 13),
    _JnxAIMContractSKUType_Type()
)
jnxAIMContractSKUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMContractSKUType.setStatus("current")


class _JnxAIMContractStartDate_Type(DisplayString):
    """Custom type jnxAIMContractStartDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMContractStartDate_Type.__name__ = "DisplayString"
_JnxAIMContractStartDate_Object = MibScalar
jnxAIMContractStartDate = _JnxAIMContractStartDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 14),
    _JnxAIMContractStartDate_Type()
)
jnxAIMContractStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMContractStartDate.setStatus("current")


class _JnxAIMContractEndDate_Type(DisplayString):
    """Custom type jnxAIMContractEndDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMContractEndDate_Type.__name__ = "DisplayString"
_JnxAIMContractEndDate_Object = MibScalar
jnxAIMContractEndDate = _JnxAIMContractEndDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 15),
    _JnxAIMContractEndDate_Type()
)
jnxAIMContractEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMContractEndDate.setStatus("current")


class _JnxAIMProduct_Type(DisplayString):
    """Custom type jnxAIMProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMProduct_Type.__name__ = "DisplayString"
_JnxAIMProduct_Object = MibScalar
jnxAIMProduct = _JnxAIMProduct_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 16),
    _JnxAIMProduct_Type()
)
jnxAIMProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMProduct.setStatus("current")


class _JnxAIMPlatform_Type(DisplayString):
    """Custom type jnxAIMPlatform based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMPlatform_Type.__name__ = "DisplayString"
_JnxAIMPlatform_Object = MibScalar
jnxAIMPlatform = _JnxAIMPlatform_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 17),
    _JnxAIMPlatform_Type()
)
jnxAIMPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMPlatform.setStatus("current")


class _JnxAIMJunosVersion_Type(DisplayString):
    """Custom type jnxAIMJunosVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMJunosVersion_Type.__name__ = "DisplayString"
_JnxAIMJunosVersion_Object = MibScalar
jnxAIMJunosVersion = _JnxAIMJunosVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 18),
    _JnxAIMJunosVersion_Type()
)
jnxAIMJunosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMJunosVersion.setStatus("current")


class _JnxAIMScriptVersion_Type(DisplayString):
    """Custom type jnxAIMScriptVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMScriptVersion_Type.__name__ = "DisplayString"
_JnxAIMScriptVersion_Object = MibScalar
jnxAIMScriptVersion = _JnxAIMScriptVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 19),
    _JnxAIMScriptVersion_Type()
)
jnxAIMScriptVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMScriptVersion.setStatus("current")


class _JnxAIMExposureMsg_Type(DisplayString):
    """Custom type jnxAIMExposureMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMExposureMsg_Type.__name__ = "DisplayString"
_JnxAIMExposureMsg_Object = MibScalar
jnxAIMExposureMsg = _JnxAIMExposureMsg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 20),
    _JnxAIMExposureMsg_Type()
)
jnxAIMExposureMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMExposureMsg.setStatus("current")


class _JnxAIMExposureIssueDate_Type(DisplayString):
    """Custom type jnxAIMExposureIssueDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMExposureIssueDate_Type.__name__ = "DisplayString"
_JnxAIMExposureIssueDate_Object = MibScalar
jnxAIMExposureIssueDate = _JnxAIMExposureIssueDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 21),
    _JnxAIMExposureIssueDate_Type()
)
jnxAIMExposureIssueDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMExposureIssueDate.setStatus("current")


class _JnxAIMExposurePRNumber_Type(DisplayString):
    """Custom type jnxAIMExposurePRNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMExposurePRNumber_Type.__name__ = "DisplayString"
_JnxAIMExposurePRNumber_Object = MibScalar
jnxAIMExposurePRNumber = _JnxAIMExposurePRNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 22),
    _JnxAIMExposurePRNumber_Type()
)
jnxAIMExposurePRNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMExposurePRNumber.setStatus("current")


class _JnxAIMExposureLink_Type(DisplayString):
    """Custom type jnxAIMExposureLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMExposureLink_Type.__name__ = "DisplayString"
_JnxAIMExposureLink_Object = MibScalar
jnxAIMExposureLink = _JnxAIMExposureLink_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 23),
    _JnxAIMExposureLink_Type()
)
jnxAIMExposureLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMExposureLink.setStatus("current")


class _JnxAIMLastIJMBReceivedTime_Type(DisplayString):
    """Custom type jnxAIMLastIJMBReceivedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMLastIJMBReceivedTime_Type.__name__ = "DisplayString"
_JnxAIMLastIJMBReceivedTime_Object = MibScalar
jnxAIMLastIJMBReceivedTime = _JnxAIMLastIJMBReceivedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 24),
    _JnxAIMLastIJMBReceivedTime_Type()
)
jnxAIMLastIJMBReceivedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMLastIJMBReceivedTime.setStatus("current")


class _JnxAIMDeviceState_Type(DisplayString):
    """Custom type jnxAIMDeviceState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMDeviceState_Type.__name__ = "DisplayString"
_JnxAIMDeviceState_Object = MibScalar
jnxAIMDeviceState = _JnxAIMDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 25),
    _JnxAIMDeviceState_Type()
)
jnxAIMDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMDeviceState.setStatus("current")


class _JnxAIMBIOSState_Type(DisplayString):
    """Custom type jnxAIMBIOSState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMBIOSState_Type.__name__ = "DisplayString"
_JnxAIMBIOSState_Object = MibScalar
jnxAIMBIOSState = _JnxAIMBIOSState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 26),
    _JnxAIMBIOSState_Type()
)
jnxAIMBIOSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMBIOSState.setStatus("current")


class _JnxAIMDaysToExpireForPartnerCert_Type(DisplayString):
    """Custom type jnxAIMDaysToExpireForPartnerCert based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMDaysToExpireForPartnerCert_Type.__name__ = "DisplayString"
_JnxAIMDaysToExpireForPartnerCert_Object = MibScalar
jnxAIMDaysToExpireForPartnerCert = _JnxAIMDaysToExpireForPartnerCert_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 27),
    _JnxAIMDaysToExpireForPartnerCert_Type()
)
jnxAIMDaysToExpireForPartnerCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMDaysToExpireForPartnerCert.setStatus("current")


class _JnxAIMExpDateTimePartnerCert_Type(DisplayString):
    """Custom type jnxAIMExpDateTimePartnerCert based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMExpDateTimePartnerCert_Type.__name__ = "DisplayString"
_JnxAIMExpDateTimePartnerCert_Object = MibScalar
jnxAIMExpDateTimePartnerCert = _JnxAIMExpDateTimePartnerCert_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 28),
    _JnxAIMExpDateTimePartnerCert_Type()
)
jnxAIMExpDateTimePartnerCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMExpDateTimePartnerCert.setStatus("current")


class _JnxAIMPHDExpectedDeviceSlot_Type(DisplayString):
    """Custom type jnxAIMPHDExpectedDeviceSlot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMPHDExpectedDeviceSlot_Type.__name__ = "DisplayString"
_JnxAIMPHDExpectedDeviceSlot_Object = MibScalar
jnxAIMPHDExpectedDeviceSlot = _JnxAIMPHDExpectedDeviceSlot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 29),
    _JnxAIMPHDExpectedDeviceSlot_Type()
)
jnxAIMPHDExpectedDeviceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMPHDExpectedDeviceSlot.setStatus("current")


class _JnxAIMPHDExpectedSNSlot_Type(DisplayString):
    """Custom type jnxAIMPHDExpectedSNSlot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMPHDExpectedSNSlot_Type.__name__ = "DisplayString"
_JnxAIMPHDExpectedSNSlot_Object = MibScalar
jnxAIMPHDExpectedSNSlot = _JnxAIMPHDExpectedSNSlot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 30),
    _JnxAIMPHDExpectedSNSlot_Type()
)
jnxAIMPHDExpectedSNSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMPHDExpectedSNSlot.setStatus("current")


class _JnxAIMPHDReceivedTime_Type(DisplayString):
    """Custom type jnxAIMPHDReceivedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMPHDReceivedTime_Type.__name__ = "DisplayString"
_JnxAIMPHDReceivedTime_Object = MibScalar
jnxAIMPHDReceivedTime = _JnxAIMPHDReceivedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 31),
    _JnxAIMPHDReceivedTime_Type()
)
jnxAIMPHDReceivedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMPHDReceivedTime.setStatus("current")


class _JnxAIMPHDFailureType_Type(DisplayString):
    """Custom type jnxAIMPHDFailureType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMPHDFailureType_Type.__name__ = "DisplayString"
_JnxAIMPHDFailureType_Object = MibScalar
jnxAIMPHDFailureType = _JnxAIMPHDFailureType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 32),
    _JnxAIMPHDFailureType_Type()
)
jnxAIMPHDFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMPHDFailureType.setStatus("current")


class _JnxAIMObjectId_Type(DisplayString):
    """Custom type jnxAIMObjectId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxAIMObjectId_Type.__name__ = "DisplayString"
_JnxAIMObjectId_Object = MibScalar
jnxAIMObjectId = _JnxAIMObjectId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 33),
    _JnxAIMObjectId_Type()
)
jnxAIMObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAIMObjectId.setStatus("current")

# Managed Objects groups


# Notification objects

jnxAIMNewIncidentDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0, 1)
)
jnxAIMNewIncidentDetected.setObjects(
      *(("JUNIPER-AI-MANAGER-MIB", "jnxAIMDescr"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMHostName"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMOrganization"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIncidentHostID"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIPAddress"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMObjectId"))
)
if mibBuilder.loadTexts:
    jnxAIMNewIncidentDetected.setStatus(
        "current"
    )

jnxAIMIncidentReportedToJuniper = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0, 2)
)
jnxAIMIncidentReportedToJuniper.setObjects(
      *(("JUNIPER-AI-MANAGER-MIB", "jnxAIMDescr"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMHostName"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMOrganization"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIncidentHostID"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIPAddress"))
)
if mibBuilder.loadTexts:
    jnxAIMIncidentReportedToJuniper.setStatus(
        "current"
    )

jnxAIMCaseIDAssigned = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0, 3)
)
jnxAIMCaseIDAssigned.setObjects(
      *(("JUNIPER-AI-MANAGER-MIB", "jnxAIMDescr"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMHostName"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMOrganization"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIncidentHostID"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMCaseID"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIPAddress"))
)
if mibBuilder.loadTexts:
    jnxAIMCaseIDAssigned.setStatus(
        "current"
    )

jnxAIMCaseUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0, 4)
)
jnxAIMCaseUpdated.setObjects(
      *(("JUNIPER-AI-MANAGER-MIB", "jnxAIMDescr"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMHostName"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMOrganization"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIncidentHostID"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMCaseID"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIPAddress"))
)
if mibBuilder.loadTexts:
    jnxAIMCaseUpdated.setStatus(
        "current"
    )

jnxAIMNewIntelligenceMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0, 5)
)
jnxAIMNewIntelligenceMessage.setObjects(
      *(("JUNIPER-AI-MANAGER-MIB", "jnxAIMDescr"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMOrganization"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIssueDate"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMObjectId"))
)
if mibBuilder.loadTexts:
    jnxAIMNewIntelligenceMessage.setStatus(
        "current"
    )

jnxAIMNewEOLMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0, 6)
)
jnxAIMNewEOLMatch.setObjects(
      *(("JUNIPER-AI-MANAGER-MIB", "jnxAIMDescr"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMHostName"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIPAddress"))
)
if mibBuilder.loadTexts:
    jnxAIMNewEOLMatch.setStatus(
        "current"
    )

jnxAIMNewPBNArrival = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0, 7)
)
jnxAIMNewPBNArrival.setObjects(
      *(("JUNIPER-AI-MANAGER-MIB", "jnxAIMDescr"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMHostName"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIPAddress"))
)
if mibBuilder.loadTexts:
    jnxAIMNewPBNArrival.setStatus(
        "current"
    )

jnxAIMNewPBNMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0, 8)
)
jnxAIMNewPBNMatch.setObjects(
    ("JUNIPER-AI-MANAGER-MIB", "jnxAIMDescr")
)
if mibBuilder.loadTexts:
    jnxAIMNewPBNMatch.setStatus(
        "current"
    )

jnxAIMContractExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0, 9)
)
jnxAIMContractExpiry.setObjects(
      *(("JUNIPER-AI-MANAGER-MIB", "jnxAIMDescr"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMHostName"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMSerialNumber"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMPartNumber"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMContractAgreementNumber"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMContractAgreementStatus"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMContractSKU"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMContractSKUType"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMContractStartDate"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMContractEndDate"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIPAddress"))
)
if mibBuilder.loadTexts:
    jnxAIMContractExpiry.setStatus(
        "current"
    )

jnxAIMNewExposure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0, 10)
)
jnxAIMNewExposure.setObjects(
      *(("JUNIPER-AI-MANAGER-MIB", "jnxAIMDescr"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMHostName"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMProduct"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMPlatform"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMJunosVersion"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMScriptVersion"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMExposureMsg"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMExposureIssueDate"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMExposurePRNumber"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMExposureLink"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIPAddress"))
)
if mibBuilder.loadTexts:
    jnxAIMNewExposure.setStatus(
        "current"
    )

jnxAIMIncidentWithoutShiptoAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0, 11)
)
jnxAIMIncidentWithoutShiptoAddress.setObjects(
      *(("JUNIPER-AI-MANAGER-MIB", "jnxAIMDescr"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMHostName"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMOrganization"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIncidentHostID"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIPAddress"))
)
if mibBuilder.loadTexts:
    jnxAIMIncidentWithoutShiptoAddress.setStatus(
        "current"
    )

jnxAIMSwitchToAutoCollectionOfIJMB = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0, 12)
)
jnxAIMSwitchToAutoCollectionOfIJMB.setObjects(
      *(("JUNIPER-AI-MANAGER-MIB", "jnxAIMDescr"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMHostName"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMProduct"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMPlatform"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMSerialNumber"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMLastIJMBReceivedTime"))
)
if mibBuilder.loadTexts:
    jnxAIMSwitchToAutoCollectionOfIJMB.setStatus(
        "current"
    )

jnxAIMConnectedMemberDeviceActions = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0, 13)
)
jnxAIMConnectedMemberDeviceActions.setObjects(
      *(("JUNIPER-AI-MANAGER-MIB", "jnxAIMDescr"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMOrganization"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMHostName"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIPAddress"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMSerialNumber"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMDeviceState"))
)
if mibBuilder.loadTexts:
    jnxAIMConnectedMemberDeviceActions.setStatus(
        "current"
    )

jnxAIMDeviceBIOSState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0, 14)
)
jnxAIMDeviceBIOSState.setObjects(
      *(("JUNIPER-AI-MANAGER-MIB", "jnxAIMDescr"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMOrganization"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMHostName"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIPAddress"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMSerialNumber"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMBIOSState"))
)
if mibBuilder.loadTexts:
    jnxAIMDeviceBIOSState.setStatus(
        "current"
    )

jnxAIMPartnerCertExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0, 15)
)
jnxAIMPartnerCertExpiry.setObjects(
      *(("JUNIPER-AI-MANAGER-MIB", "jnxAIMDaysToExpireForPartnerCert"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMExpDateTimePartnerCert"))
)
if mibBuilder.loadTexts:
    jnxAIMPartnerCertExpiry.setStatus(
        "current"
    )

jnxAIMPartnerCertExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0, 16)
)
jnxAIMPartnerCertExpired.setObjects(
    ("JUNIPER-AI-MANAGER-MIB", "jnxAIMExpDateTimePartnerCert")
)
if mibBuilder.loadTexts:
    jnxAIMPartnerCertExpired.setStatus(
        "current"
    )

jnxAIMPHDCollectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 9, 1, 0, 17)
)
jnxAIMPHDCollectionFailure.setObjects(
      *(("JUNIPER-AI-MANAGER-MIB", "jnxAIMDescr"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMHostName"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMIPAddress"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMPHDFailureType"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMPHDReceivedTime"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMPHDExpectedDeviceSlot"),
        ("JUNIPER-AI-MANAGER-MIB", "jnxAIMPHDExpectedSNSlot"))
)
if mibBuilder.loadTexts:
    jnxAIMPHDCollectionFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-AI-MANAGER-MIB",
    **{"jnxAIManager": jnxAIManager,
       "jnxAIManagerNotifications": jnxAIManagerNotifications,
       "jnxAIMNewIncidentDetected": jnxAIMNewIncidentDetected,
       "jnxAIMIncidentReportedToJuniper": jnxAIMIncidentReportedToJuniper,
       "jnxAIMCaseIDAssigned": jnxAIMCaseIDAssigned,
       "jnxAIMCaseUpdated": jnxAIMCaseUpdated,
       "jnxAIMNewIntelligenceMessage": jnxAIMNewIntelligenceMessage,
       "jnxAIMNewEOLMatch": jnxAIMNewEOLMatch,
       "jnxAIMNewPBNArrival": jnxAIMNewPBNArrival,
       "jnxAIMNewPBNMatch": jnxAIMNewPBNMatch,
       "jnxAIMContractExpiry": jnxAIMContractExpiry,
       "jnxAIMNewExposure": jnxAIMNewExposure,
       "jnxAIMIncidentWithoutShiptoAddress": jnxAIMIncidentWithoutShiptoAddress,
       "jnxAIMSwitchToAutoCollectionOfIJMB": jnxAIMSwitchToAutoCollectionOfIJMB,
       "jnxAIMConnectedMemberDeviceActions": jnxAIMConnectedMemberDeviceActions,
       "jnxAIMDeviceBIOSState": jnxAIMDeviceBIOSState,
       "jnxAIMPartnerCertExpiry": jnxAIMPartnerCertExpiry,
       "jnxAIMPartnerCertExpired": jnxAIMPartnerCertExpired,
       "jnxAIMPHDCollectionFailure": jnxAIMPHDCollectionFailure,
       "jnxAIMDescr": jnxAIMDescr,
       "jnxAIMHostName": jnxAIMHostName,
       "jnxAIMOrganization": jnxAIMOrganization,
       "jnxAIMIncidentHostID": jnxAIMIncidentHostID,
       "jnxAIMCaseID": jnxAIMCaseID,
       "jnxAIMIssueDate": jnxAIMIssueDate,
       "jnxAIMIPAddress": jnxAIMIPAddress,
       "jnxAIMSerialNumber": jnxAIMSerialNumber,
       "jnxAIMPartNumber": jnxAIMPartNumber,
       "jnxAIMContractAgreementNumber": jnxAIMContractAgreementNumber,
       "jnxAIMContractAgreementStatus": jnxAIMContractAgreementStatus,
       "jnxAIMContractSKU": jnxAIMContractSKU,
       "jnxAIMContractSKUType": jnxAIMContractSKUType,
       "jnxAIMContractStartDate": jnxAIMContractStartDate,
       "jnxAIMContractEndDate": jnxAIMContractEndDate,
       "jnxAIMProduct": jnxAIMProduct,
       "jnxAIMPlatform": jnxAIMPlatform,
       "jnxAIMJunosVersion": jnxAIMJunosVersion,
       "jnxAIMScriptVersion": jnxAIMScriptVersion,
       "jnxAIMExposureMsg": jnxAIMExposureMsg,
       "jnxAIMExposureIssueDate": jnxAIMExposureIssueDate,
       "jnxAIMExposurePRNumber": jnxAIMExposurePRNumber,
       "jnxAIMExposureLink": jnxAIMExposureLink,
       "jnxAIMLastIJMBReceivedTime": jnxAIMLastIJMBReceivedTime,
       "jnxAIMDeviceState": jnxAIMDeviceState,
       "jnxAIMBIOSState": jnxAIMBIOSState,
       "jnxAIMDaysToExpireForPartnerCert": jnxAIMDaysToExpireForPartnerCert,
       "jnxAIMExpDateTimePartnerCert": jnxAIMExpDateTimePartnerCert,
       "jnxAIMPHDExpectedDeviceSlot": jnxAIMPHDExpectedDeviceSlot,
       "jnxAIMPHDExpectedSNSlot": jnxAIMPHDExpectedSNSlot,
       "jnxAIMPHDReceivedTime": jnxAIMPHDReceivedTime,
       "jnxAIMPHDFailureType": jnxAIMPHDFailureType,
       "jnxAIMObjectId": jnxAIMObjectId}
)
