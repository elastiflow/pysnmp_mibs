# SNMP MIB module (A3COM-HUAWEI-IDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-IDS-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:04:11 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

h3cIDSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cIds_ObjectIdentity = ObjectIdentity
h3cIds = _H3cIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47)
)
_H3cIDSTrapGroup_ObjectIdentity = ObjectIdentity
h3cIDSTrapGroup = _H3cIDSTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1)
)
_H3cIDSTrapInfo_ObjectIdentity = ObjectIdentity
h3cIDSTrapInfo = _H3cIDSTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1)
)
_H3cIDSTrapIPFragmentQueueLen_Type = Unsigned32
_H3cIDSTrapIPFragmentQueueLen_Object = MibScalar
h3cIDSTrapIPFragmentQueueLen = _H3cIDSTrapIPFragmentQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 1),
    _H3cIDSTrapIPFragmentQueueLen_Type()
)
h3cIDSTrapIPFragmentQueueLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIDSTrapIPFragmentQueueLen.setStatus("current")
_H3cIDSTrapStatSessionTabLen_Type = Unsigned32
_H3cIDSTrapStatSessionTabLen_Object = MibScalar
h3cIDSTrapStatSessionTabLen = _H3cIDSTrapStatSessionTabLen_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 2),
    _H3cIDSTrapStatSessionTabLen_Type()
)
h3cIDSTrapStatSessionTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIDSTrapStatSessionTabLen.setStatus("current")
_H3cIDSTrapIPAddressType_Type = InetAddressType
_H3cIDSTrapIPAddressType_Object = MibScalar
h3cIDSTrapIPAddressType = _H3cIDSTrapIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 3),
    _H3cIDSTrapIPAddressType_Type()
)
h3cIDSTrapIPAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIDSTrapIPAddressType.setStatus("current")
_H3cIDSTrapIPAddress_Type = InetAddress
_H3cIDSTrapIPAddress_Object = MibScalar
h3cIDSTrapIPAddress = _H3cIDSTrapIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 4),
    _H3cIDSTrapIPAddress_Type()
)
h3cIDSTrapIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIDSTrapIPAddress.setStatus("current")


class _H3cIDSTrapUserName_Type(OctetString):
    """Custom type h3cIDSTrapUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cIDSTrapUserName_Type.__name__ = "OctetString"
_H3cIDSTrapUserName_Object = MibScalar
h3cIDSTrapUserName = _H3cIDSTrapUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 5),
    _H3cIDSTrapUserName_Type()
)
h3cIDSTrapUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIDSTrapUserName.setStatus("current")


class _H3cIDSTrapLoginType_Type(Integer32):
    """Custom type h3cIDSTrapLoginType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("telnet", 1),
          ("ssh", 2),
          ("web", 3))
    )


_H3cIDSTrapLoginType_Type.__name__ = "Integer32"
_H3cIDSTrapLoginType_Object = MibScalar
h3cIDSTrapLoginType = _H3cIDSTrapLoginType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 6),
    _H3cIDSTrapLoginType_Type()
)
h3cIDSTrapLoginType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIDSTrapLoginType.setStatus("current")


class _H3cIDSTrapUpgradeType_Type(Integer32):
    """Custom type h3cIDSTrapUpgradeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("programme", 1),
          ("crb", 2),
          ("vrb", 3))
    )


_H3cIDSTrapUpgradeType_Type.__name__ = "Integer32"
_H3cIDSTrapUpgradeType_Object = MibScalar
h3cIDSTrapUpgradeType = _H3cIDSTrapUpgradeType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 7),
    _H3cIDSTrapUpgradeType_Type()
)
h3cIDSTrapUpgradeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIDSTrapUpgradeType.setStatus("current")


class _H3cIDSTrapCRLName_Type(OctetString):
    """Custom type h3cIDSTrapCRLName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cIDSTrapCRLName_Type.__name__ = "OctetString"
_H3cIDSTrapCRLName_Object = MibScalar
h3cIDSTrapCRLName = _H3cIDSTrapCRLName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 8),
    _H3cIDSTrapCRLName_Type()
)
h3cIDSTrapCRLName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIDSTrapCRLName.setStatus("current")


class _H3cIDSTrapCertName_Type(OctetString):
    """Custom type h3cIDSTrapCertName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cIDSTrapCertName_Type.__name__ = "OctetString"
_H3cIDSTrapCertName_Object = MibScalar
h3cIDSTrapCertName = _H3cIDSTrapCertName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 9),
    _H3cIDSTrapCertName_Type()
)
h3cIDSTrapCertName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIDSTrapCertName.setStatus("current")
_H3cIDSTrapDetectRuleID_Type = Unsigned32
_H3cIDSTrapDetectRuleID_Object = MibScalar
h3cIDSTrapDetectRuleID = _H3cIDSTrapDetectRuleID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 10),
    _H3cIDSTrapDetectRuleID_Type()
)
h3cIDSTrapDetectRuleID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIDSTrapDetectRuleID.setStatus("current")
_H3cIDSTrapEngineID_Type = Integer32
_H3cIDSTrapEngineID_Object = MibScalar
h3cIDSTrapEngineID = _H3cIDSTrapEngineID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 11),
    _H3cIDSTrapEngineID_Type()
)
h3cIDSTrapEngineID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIDSTrapEngineID.setStatus("current")


class _H3cIDSTrapFileName_Type(OctetString):
    """Custom type h3cIDSTrapFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_H3cIDSTrapFileName_Type.__name__ = "OctetString"
_H3cIDSTrapFileName_Object = MibScalar
h3cIDSTrapFileName = _H3cIDSTrapFileName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 12),
    _H3cIDSTrapFileName_Type()
)
h3cIDSTrapFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIDSTrapFileName.setStatus("current")
_H3cIDSTrapCfgLineInFile_Type = Unsigned32
_H3cIDSTrapCfgLineInFile_Object = MibScalar
h3cIDSTrapCfgLineInFile = _H3cIDSTrapCfgLineInFile_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 13),
    _H3cIDSTrapCfgLineInFile_Type()
)
h3cIDSTrapCfgLineInFile.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIDSTrapCfgLineInFile.setStatus("current")


class _H3cIDSTrapReasonForError_Type(OctetString):
    """Custom type h3cIDSTrapReasonForError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_H3cIDSTrapReasonForError_Type.__name__ = "OctetString"
_H3cIDSTrapReasonForError_Object = MibScalar
h3cIDSTrapReasonForError = _H3cIDSTrapReasonForError_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 1, 14),
    _H3cIDSTrapReasonForError_Type()
)
h3cIDSTrapReasonForError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIDSTrapReasonForError.setStatus("current")
_H3cIDSTrap_ObjectIdentity = ObjectIdentity
h3cIDSTrap = _H3cIDSTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2)
)
_H3cIDSTrapPrefix_ObjectIdentity = ObjectIdentity
h3cIDSTrapPrefix = _H3cIDSTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0)
)

# Managed Objects groups


# Notification objects

h3cIDSTrapIPFragQueueFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 1)
)
h3cIDSTrapIPFragQueueFull.setObjects(
      *(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapIPFragmentQueueLen"),
        ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    h3cIDSTrapIPFragQueueFull.setStatus(
        "current"
    )

h3cIDSTrapStatSessTabFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 2)
)
h3cIDSTrapStatSessTabFull.setObjects(
      *(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapStatSessionTabLen"),
        ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    h3cIDSTrapStatSessTabFull.setStatus(
        "current"
    )

h3cIDSTrapDetectRuleParseFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 3)
)
h3cIDSTrapDetectRuleParseFail.setObjects(
      *(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapDetectRuleID"),
        ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapEngineID"),
        ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    h3cIDSTrapDetectRuleParseFail.setStatus(
        "current"
    )

h3cIDSTrapDBConnLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 4)
)
h3cIDSTrapDBConnLost.setObjects(
      *(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapIPAddressType"),
        ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapIPAddress"),
        ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    h3cIDSTrapDBConnLost.setStatus(
        "current"
    )

h3cIDSTrapCRLNeedUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 5)
)
h3cIDSTrapCRLNeedUpdate.setObjects(
      *(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapCRLName"),
        ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    h3cIDSTrapCRLNeedUpdate.setStatus(
        "current"
    )

h3cIDSTrapCertOverdue = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 6)
)
h3cIDSTrapCertOverdue.setObjects(
      *(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapCertName"),
        ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    h3cIDSTrapCertOverdue.setStatus(
        "current"
    )

h3cIDSTrapTooManyLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 7)
)
h3cIDSTrapTooManyLoginFail.setObjects(
      *(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapUserName"),
        ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapIPAddressType"),
        ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapIPAddress"),
        ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapLoginType"),
        ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    h3cIDSTrapTooManyLoginFail.setStatus(
        "current"
    )

h3cIDSTrapUpgradeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 8)
)
h3cIDSTrapUpgradeError.setObjects(
      *(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapUpgradeType"),
        ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    h3cIDSTrapUpgradeError.setStatus(
        "current"
    )

h3cIDSTrapFileAccessError = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 9)
)
h3cIDSTrapFileAccessError.setObjects(
      *(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapFileName"),
        ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError"))
)
if mibBuilder.loadTexts:
    h3cIDSTrapFileAccessError.setStatus(
        "current"
    )

h3cIDSTrapConsArithMemLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 10)
)
h3cIDSTrapConsArithMemLow.setObjects(
    ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError")
)
if mibBuilder.loadTexts:
    h3cIDSTrapConsArithMemLow.setStatus(
        "current"
    )

h3cIDSTrapSSRAMOperFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 11)
)
h3cIDSTrapSSRAMOperFail.setObjects(
    ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError")
)
if mibBuilder.loadTexts:
    h3cIDSTrapSSRAMOperFail.setStatus(
        "current"
    )

h3cIDSTrapPacketProcessDisorder = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 12)
)
h3cIDSTrapPacketProcessDisorder.setObjects(
    ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapReasonForError")
)
if mibBuilder.loadTexts:
    h3cIDSTrapPacketProcessDisorder.setStatus(
        "current"
    )

h3cIDSTrapCfgFileFormatError = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 47, 1, 1, 2, 0, 13)
)
h3cIDSTrapCfgFileFormatError.setObjects(
      *(("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapFileName"),
        ("A3COM-HUAWEI-IDS-MIB", "h3cIDSTrapCfgLineInFile"))
)
if mibBuilder.loadTexts:
    h3cIDSTrapCfgFileFormatError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-IDS-MIB",
    **{"h3cIds": h3cIds,
       "h3cIDSMib": h3cIDSMib,
       "h3cIDSTrapGroup": h3cIDSTrapGroup,
       "h3cIDSTrapInfo": h3cIDSTrapInfo,
       "h3cIDSTrapIPFragmentQueueLen": h3cIDSTrapIPFragmentQueueLen,
       "h3cIDSTrapStatSessionTabLen": h3cIDSTrapStatSessionTabLen,
       "h3cIDSTrapIPAddressType": h3cIDSTrapIPAddressType,
       "h3cIDSTrapIPAddress": h3cIDSTrapIPAddress,
       "h3cIDSTrapUserName": h3cIDSTrapUserName,
       "h3cIDSTrapLoginType": h3cIDSTrapLoginType,
       "h3cIDSTrapUpgradeType": h3cIDSTrapUpgradeType,
       "h3cIDSTrapCRLName": h3cIDSTrapCRLName,
       "h3cIDSTrapCertName": h3cIDSTrapCertName,
       "h3cIDSTrapDetectRuleID": h3cIDSTrapDetectRuleID,
       "h3cIDSTrapEngineID": h3cIDSTrapEngineID,
       "h3cIDSTrapFileName": h3cIDSTrapFileName,
       "h3cIDSTrapCfgLineInFile": h3cIDSTrapCfgLineInFile,
       "h3cIDSTrapReasonForError": h3cIDSTrapReasonForError,
       "h3cIDSTrap": h3cIDSTrap,
       "h3cIDSTrapPrefix": h3cIDSTrapPrefix,
       "h3cIDSTrapIPFragQueueFull": h3cIDSTrapIPFragQueueFull,
       "h3cIDSTrapStatSessTabFull": h3cIDSTrapStatSessTabFull,
       "h3cIDSTrapDetectRuleParseFail": h3cIDSTrapDetectRuleParseFail,
       "h3cIDSTrapDBConnLost": h3cIDSTrapDBConnLost,
       "h3cIDSTrapCRLNeedUpdate": h3cIDSTrapCRLNeedUpdate,
       "h3cIDSTrapCertOverdue": h3cIDSTrapCertOverdue,
       "h3cIDSTrapTooManyLoginFail": h3cIDSTrapTooManyLoginFail,
       "h3cIDSTrapUpgradeError": h3cIDSTrapUpgradeError,
       "h3cIDSTrapFileAccessError": h3cIDSTrapFileAccessError,
       "h3cIDSTrapConsArithMemLow": h3cIDSTrapConsArithMemLow,
       "h3cIDSTrapSSRAMOperFail": h3cIDSTrapSSRAMOperFail,
       "h3cIDSTrapPacketProcessDisorder": h3cIDSTrapPacketProcessDisorder,
       "h3cIDSTrapCfgFileFormatError": h3cIDSTrapCfgFileFormatError}
)
