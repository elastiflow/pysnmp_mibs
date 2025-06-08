# SNMP MIB module (CL-PKTC-EUE-RST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/CL-PKTC-EUE-RST-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:37:34 2025
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

(pktcEUEDevOpIndex,) = mibBuilder.importSymbols(
    "CL-PKTC-EUE-DEV-MIB",
    "pktcEUEDevOpIndex")

(PktcEUETCAdminStatus,
 PktcEUETCOperStatus,
 PktcEUETCStatusInfo,
 PktcEUETCUsrAppIndexType) = mibBuilder.importSymbols(
    "CL-PKTC-EUE-TC-MIB",
    "PktcEUETCAdminStatus",
    "PktcEUETCOperStatus",
    "PktcEUETCStatusInfo",
    "PktcEUETCUsrAppIndexType")

(pktcApplicationMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcApplicationMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(Uri,) = mibBuilder.importSymbols(
    "URI-TC-MIB",
    "Uri")


# MODULE-IDENTITY

pktcEUERSTMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2)
)
if mibBuilder.loadTexts:
    pktcEUERSTMIB.setRevisions(
        ("2011-04-01 00:00",
         "2010-04-26 00:00",
         "2009-12-14 00:00",
         "2009-05-28 00:00",
         "2008-07-10 00:00",
         "2007-11-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PktcRSTTCFeatID(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("digitMap", 2),
          ("basicCall", 3),
          ("announcement", 4),
          ("statusChange", 5),
          ("noAnsTimeout", 6),
          ("callerId", 7),
          ("callerIdDisplay", 8),
          ("callerIdBlocking", 9),
          ("callerIdDelivery", 10),
          ("callForwarding", 11),
          ("callWaiting", 12),
          ("callHold", 13),
          ("callTransfer", 14),
          ("threeWayCalling", 15),
          ("doNotDisturb", 16),
          ("subscrProgPin", 17),
          ("msgWaitIndicator", 18),
          ("autoRecall", 19),
          ("autoCallback", 20),
          ("busyLineVerify", 21),
          ("emergencySvc", 22),
          ("scf", 23),
          ("acr", 24),
          ("solicitorBlocking", 25),
          ("distinctAlerting", 26),
          ("speedDialing", 27),
          ("cot", 28),
          ("heldMedia", 29),
          ("localSpeedDialing", 30),
          ("hotline", 31),
          ("digitMapVariable", 32))
    )



class PktcEUETCRSTAppFeatIndexType(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class PktcEUETCRSTAUID(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"


# MIB Managed Objects in the order of their OIDs

_PktcEUERSTNotifications_ObjectIdentity = ObjectIdentity
pktcEUERSTNotifications = _PktcEUERSTNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 0)
)
_PktcEUERSTObjects_ObjectIdentity = ObjectIdentity
pktcEUERSTObjects = _PktcEUERSTObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1)
)
_PktcEUERSTProfile_ObjectIdentity = ObjectIdentity
pktcEUERSTProfile = _PktcEUERSTProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1)
)


class _PktcEUERSTProfileVersion_Type(SnmpAdminString):
    """Custom type pktcEUERSTProfileVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_PktcEUERSTProfileVersion_Type.__name__ = "SnmpAdminString"
_PktcEUERSTProfileVersion_Object = MibScalar
pktcEUERSTProfileVersion = _PktcEUERSTProfileVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 1),
    _PktcEUERSTProfileVersion_Type()
)
pktcEUERSTProfileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUERSTProfileVersion.setStatus("current")
_PktcEUERSTAppProfileToFeatTable_Object = MibTable
pktcEUERSTAppProfileToFeatTable = _PktcEUERSTAppProfileToFeatTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pktcEUERSTAppProfileToFeatTable.setStatus("current")
_PktcEUERSTAppProfileToFeatEntry_Object = MibTableRow
pktcEUERSTAppProfileToFeatEntry = _PktcEUERSTAppProfileToFeatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1)
)
pktcEUERSTAppProfileToFeatEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppProfileIndex"),
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppFeatIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTAppProfileToFeatEntry.setStatus("current")
_PktcEUERSTAppProfileIndex_Type = PktcEUETCUsrAppIndexType
_PktcEUERSTAppProfileIndex_Object = MibTableColumn
pktcEUERSTAppProfileIndex = _PktcEUERSTAppProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 1),
    _PktcEUERSTAppProfileIndex_Type()
)
pktcEUERSTAppProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTAppProfileIndex.setStatus("current")
_PktcEUERSTAppFeatIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTAppFeatIndex_Object = MibTableColumn
pktcEUERSTAppFeatIndex = _PktcEUERSTAppFeatIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 2),
    _PktcEUERSTAppFeatIndex_Type()
)
pktcEUERSTAppFeatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTAppFeatIndex.setStatus("current")
_PktcEUERSTAppFeatID_Type = PktcRSTTCFeatID
_PktcEUERSTAppFeatID_Object = MibTableColumn
pktcEUERSTAppFeatID = _PktcEUERSTAppFeatID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 3),
    _PktcEUERSTAppFeatID_Type()
)
pktcEUERSTAppFeatID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTAppFeatID.setStatus("current")
_PktcEUERSTAppFeatIndexRef_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTAppFeatIndexRef_Object = MibTableColumn
pktcEUERSTAppFeatIndexRef = _PktcEUERSTAppFeatIndexRef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 4),
    _PktcEUERSTAppFeatIndexRef_Type()
)
pktcEUERSTAppFeatIndexRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTAppFeatIndexRef.setStatus("current")


class _PktcEUERSTAppAdminStat_Type(PktcEUETCAdminStatus):
    """Custom type pktcEUERSTAppAdminStat based on PktcEUETCAdminStatus"""
    defaultValue = 1


_PktcEUERSTAppAdminStat_Type.__name__ = "PktcEUETCAdminStatus"
_PktcEUERSTAppAdminStat_Object = MibTableColumn
pktcEUERSTAppAdminStat = _PktcEUERSTAppAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 5),
    _PktcEUERSTAppAdminStat_Type()
)
pktcEUERSTAppAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTAppAdminStat.setStatus("current")


class _PktcEUERSTAppAdminStatInfo_Type(PktcEUETCStatusInfo):
    """Custom type pktcEUERSTAppAdminStatInfo based on PktcEUETCStatusInfo"""
    defaultValue = OctetString("")


_PktcEUERSTAppAdminStatInfo_Type.__name__ = "PktcEUETCStatusInfo"
_PktcEUERSTAppAdminStatInfo_Object = MibTableColumn
pktcEUERSTAppAdminStatInfo = _PktcEUERSTAppAdminStatInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 6),
    _PktcEUERSTAppAdminStatInfo_Type()
)
pktcEUERSTAppAdminStatInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTAppAdminStatInfo.setStatus("current")
_PktcEUERSTAppOperStat_Type = PktcEUETCOperStatus
_PktcEUERSTAppOperStat_Object = MibTableColumn
pktcEUERSTAppOperStat = _PktcEUERSTAppOperStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 7),
    _PktcEUERSTAppOperStat_Type()
)
pktcEUERSTAppOperStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUERSTAppOperStat.setStatus("current")


class _PktcEUERSTAppOperStatInfo_Type(PktcEUETCStatusInfo):
    """Custom type pktcEUERSTAppOperStatInfo based on PktcEUETCStatusInfo"""
    defaultValue = OctetString("")


_PktcEUERSTAppOperStatInfo_Type.__name__ = "PktcEUETCStatusInfo"
_PktcEUERSTAppOperStatInfo_Object = MibTableColumn
pktcEUERSTAppOperStatInfo = _PktcEUERSTAppOperStatInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 8),
    _PktcEUERSTAppOperStatInfo_Type()
)
pktcEUERSTAppOperStatInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUERSTAppOperStatInfo.setStatus("current")
_PktcEUERSTAppStatus_Type = RowStatus
_PktcEUERSTAppStatus_Object = MibTableColumn
pktcEUERSTAppStatus = _PktcEUERSTAppStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 9),
    _PktcEUERSTAppStatus_Type()
)
pktcEUERSTAppStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTAppStatus.setStatus("current")
_PktcEUERSTDigitMapFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTDigitMapFeat = _PktcEUERSTDigitMapFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3)
)
_PktcEUERSTDigitMapProfileTable_Object = MibTable
pktcEUERSTDigitMapProfileTable = _PktcEUERSTDigitMapProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTDigitMapProfileTable.setStatus("current")
_PktcEUERSTDigitMapProfileEntry_Object = MibTableRow
pktcEUERSTDigitMapProfileEntry = _PktcEUERSTDigitMapProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 1, 1)
)
pktcEUERSTDigitMapProfileEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTDMIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTDigitMapProfileEntry.setStatus("current")
_PktcEUERSTDMIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTDMIndex_Object = MibTableColumn
pktcEUERSTDMIndex = _PktcEUERSTDMIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 1, 1, 1),
    _PktcEUERSTDMIndex_Type()
)
pktcEUERSTDMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTDMIndex.setStatus("current")


class _PktcEUERSTDMValue_Type(OctetString):
    """Custom type pktcEUERSTDMValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_PktcEUERSTDMValue_Type.__name__ = "OctetString"
_PktcEUERSTDMValue_Object = MibTableColumn
pktcEUERSTDMValue = _PktcEUERSTDMValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 1, 1, 2),
    _PktcEUERSTDMValue_Type()
)
pktcEUERSTDMValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTDMValue.setStatus("current")
_PktcEUERSTDMStatus_Type = RowStatus
_PktcEUERSTDMStatus_Object = MibTableColumn
pktcEUERSTDMStatus = _PktcEUERSTDMStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 1, 1, 3),
    _PktcEUERSTDMStatus_Type()
)
pktcEUERSTDMStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTDMStatus.setStatus("current")
_PktcEUERSTDigitMapVariableTable_Object = MibTable
pktcEUERSTDigitMapVariableTable = _PktcEUERSTDigitMapVariableTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    pktcEUERSTDigitMapVariableTable.setStatus("current")
_PktcEUERSTDigitMapVariableEntry_Object = MibTableRow
pktcEUERSTDigitMapVariableEntry = _PktcEUERSTDigitMapVariableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 2, 1)
)
pktcEUERSTDigitMapVariableEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTDigitMapVariableIndex"),
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTDigitMapVariableId"),
)
if mibBuilder.loadTexts:
    pktcEUERSTDigitMapVariableEntry.setStatus("current")
_PktcEUERSTDigitMapVariableIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTDigitMapVariableIndex_Object = MibTableColumn
pktcEUERSTDigitMapVariableIndex = _PktcEUERSTDigitMapVariableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 2, 1, 1),
    _PktcEUERSTDigitMapVariableIndex_Type()
)
pktcEUERSTDigitMapVariableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTDigitMapVariableIndex.setStatus("current")


class _PktcEUERSTDigitMapVariableId_Type(Unsigned32):
    """Custom type pktcEUERSTDigitMapVariableId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PktcEUERSTDigitMapVariableId_Type.__name__ = "Unsigned32"
_PktcEUERSTDigitMapVariableId_Object = MibTableColumn
pktcEUERSTDigitMapVariableId = _PktcEUERSTDigitMapVariableId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 2, 1, 2),
    _PktcEUERSTDigitMapVariableId_Type()
)
pktcEUERSTDigitMapVariableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTDigitMapVariableId.setStatus("current")
_PktcEUERSTDigitMapVariableName_Type = SnmpAdminString
_PktcEUERSTDigitMapVariableName_Object = MibTableColumn
pktcEUERSTDigitMapVariableName = _PktcEUERSTDigitMapVariableName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 2, 1, 3),
    _PktcEUERSTDigitMapVariableName_Type()
)
pktcEUERSTDigitMapVariableName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTDigitMapVariableName.setStatus("current")
_PktcEUERSTDigitMapVariableValue_Type = SnmpAdminString
_PktcEUERSTDigitMapVariableValue_Object = MibTableColumn
pktcEUERSTDigitMapVariableValue = _PktcEUERSTDigitMapVariableValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 2, 1, 4),
    _PktcEUERSTDigitMapVariableValue_Type()
)
pktcEUERSTDigitMapVariableValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTDigitMapVariableValue.setStatus("current")
_PktcEUERSTDigitMapVariableStatus_Type = RowStatus
_PktcEUERSTDigitMapVariableStatus_Object = MibTableColumn
pktcEUERSTDigitMapVariableStatus = _PktcEUERSTDigitMapVariableStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 2, 1, 5),
    _PktcEUERSTDigitMapVariableStatus_Type()
)
pktcEUERSTDigitMapVariableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTDigitMapVariableStatus.setStatus("current")
_PktcEUERSTKeepAlive_Type = TruthValue
_PktcEUERSTKeepAlive_Object = MibScalar
pktcEUERSTKeepAlive = _PktcEUERSTKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 4),
    _PktcEUERSTKeepAlive_Type()
)
pktcEUERSTKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTKeepAlive.setStatus("deprecated")


class _PktcEUERSTKeepAliveSetting_Type(Integer32):
    """Custom type pktcEUERSTKeepAliveSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("conditional", 3))
    )


_PktcEUERSTKeepAliveSetting_Type.__name__ = "Integer32"
_PktcEUERSTKeepAliveSetting_Object = MibScalar
pktcEUERSTKeepAliveSetting = _PktcEUERSTKeepAliveSetting_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 5),
    _PktcEUERSTKeepAliveSetting_Type()
)
pktcEUERSTKeepAliveSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTKeepAliveSetting.setStatus("current")
_PktcEUERSTFeatures_ObjectIdentity = ObjectIdentity
pktcEUERSTFeatures = _PktcEUERSTFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2)
)
_PktcEUERSTBasicCallFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTBasicCallFeat = _PktcEUERSTBasicCallFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1)
)
_PktcEUERSTBasicCallTable_Object = MibTable
pktcEUERSTBasicCallTable = _PktcEUERSTBasicCallTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTBasicCallTable.setStatus("current")
_PktcEUERSTBasicCallEntry_Object = MibTableRow
pktcEUERSTBasicCallEntry = _PktcEUERSTBasicCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 1, 1)
)
pktcEUERSTBasicCallEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTBCallIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTBasicCallEntry.setStatus("current")
_PktcEUERSTBCallIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTBCallIndex_Object = MibTableColumn
pktcEUERSTBCallIndex = _PktcEUERSTBCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 1, 1, 1),
    _PktcEUERSTBCallIndex_Type()
)
pktcEUERSTBCallIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTBCallIndex.setStatus("current")
_PktcEUERSTBCallPrefCodecList_Type = SnmpAdminString
_PktcEUERSTBCallPrefCodecList_Object = MibTableColumn
pktcEUERSTBCallPrefCodecList = _PktcEUERSTBCallPrefCodecList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 1, 1, 2),
    _PktcEUERSTBCallPrefCodecList_Type()
)
pktcEUERSTBCallPrefCodecList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTBCallPrefCodecList.setStatus("current")
_PktcEUERSTBCallStatus_Type = RowStatus
_PktcEUERSTBCallStatus_Object = MibTableColumn
pktcEUERSTBCallStatus = _PktcEUERSTBCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 1, 1, 3),
    _PktcEUERSTBCallStatus_Type()
)
pktcEUERSTBCallStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTBCallStatus.setStatus("current")
_PktcEUERSTNfBasicCallTable_Object = MibTable
pktcEUERSTNfBasicCallTable = _PktcEUERSTNfBasicCallTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfBasicCallTable.setStatus("current")
_PktcEUERSTNfBasicCallEntry_Object = MibTableRow
pktcEUERSTNfBasicCallEntry = _PktcEUERSTNfBasicCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1)
)
pktcEUERSTNfBasicCallEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfBasicCallEntry.setStatus("current")
_PktcEUERSTNfBCallByeDelay_Type = Unsigned32
_PktcEUERSTNfBCallByeDelay_Object = MibTableColumn
pktcEUERSTNfBCallByeDelay = _PktcEUERSTNfBCallByeDelay_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 1),
    _PktcEUERSTNfBCallByeDelay_Type()
)
pktcEUERSTNfBCallByeDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallByeDelay.setStatus("current")
_PktcEUERSTNfBCallOrigDTTimer_Type = Unsigned32
_PktcEUERSTNfBCallOrigDTTimer_Object = MibTableColumn
pktcEUERSTNfBCallOrigDTTimer = _PktcEUERSTNfBCallOrigDTTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 2),
    _PktcEUERSTNfBCallOrigDTTimer_Type()
)
pktcEUERSTNfBCallOrigDTTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallOrigDTTimer.setStatus("current")
_PktcEUERSTNfBCallTermOHErrSig_Type = Uri
_PktcEUERSTNfBCallTermOHErrSig_Object = MibTableColumn
pktcEUERSTNfBCallTermOHErrSig = _PktcEUERSTNfBCallTermOHErrSig_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 3),
    _PktcEUERSTNfBCallTermOHErrSig_Type()
)
pktcEUERSTNfBCallTermOHErrSig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallTermOHErrSig.setStatus("current")
_PktcEUERSTNfBCallTermErrSigTimer_Type = Unsigned32
_PktcEUERSTNfBCallTermErrSigTimer_Object = MibTableColumn
pktcEUERSTNfBCallTermErrSigTimer = _PktcEUERSTNfBCallTermErrSigTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 4),
    _PktcEUERSTNfBCallTermErrSigTimer_Type()
)
pktcEUERSTNfBCallTermErrSigTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallTermErrSigTimer.setStatus("current")
_PktcEUERSTNfBCallPermSeqTone1_Type = Uri
_PktcEUERSTNfBCallPermSeqTone1_Object = MibTableColumn
pktcEUERSTNfBCallPermSeqTone1 = _PktcEUERSTNfBCallPermSeqTone1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 5),
    _PktcEUERSTNfBCallPermSeqTone1_Type()
)
pktcEUERSTNfBCallPermSeqTone1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallPermSeqTone1.setStatus("current")
_PktcEUERSTNfBCallPermSeqTimer1_Type = Unsigned32
_PktcEUERSTNfBCallPermSeqTimer1_Object = MibTableColumn
pktcEUERSTNfBCallPermSeqTimer1 = _PktcEUERSTNfBCallPermSeqTimer1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 6),
    _PktcEUERSTNfBCallPermSeqTimer1_Type()
)
pktcEUERSTNfBCallPermSeqTimer1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallPermSeqTimer1.setStatus("current")
_PktcEUERSTNfBCallPermSeqTone2_Type = Uri
_PktcEUERSTNfBCallPermSeqTone2_Object = MibTableColumn
pktcEUERSTNfBCallPermSeqTone2 = _PktcEUERSTNfBCallPermSeqTone2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 7),
    _PktcEUERSTNfBCallPermSeqTone2_Type()
)
pktcEUERSTNfBCallPermSeqTone2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallPermSeqTone2.setStatus("current")
_PktcEUERSTNfBCallPermSeqTimer2_Type = Unsigned32
_PktcEUERSTNfBCallPermSeqTimer2_Object = MibTableColumn
pktcEUERSTNfBCallPermSeqTimer2 = _PktcEUERSTNfBCallPermSeqTimer2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 8),
    _PktcEUERSTNfBCallPermSeqTimer2_Type()
)
pktcEUERSTNfBCallPermSeqTimer2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallPermSeqTimer2.setStatus("current")
_PktcEUERSTNfBCallPermSeqTone3_Type = Uri
_PktcEUERSTNfBCallPermSeqTone3_Object = MibTableColumn
pktcEUERSTNfBCallPermSeqTone3 = _PktcEUERSTNfBCallPermSeqTone3_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 9),
    _PktcEUERSTNfBCallPermSeqTone3_Type()
)
pktcEUERSTNfBCallPermSeqTone3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallPermSeqTone3.setStatus("current")
_PktcEUERSTNfBCallPermSeqTimer3_Type = Unsigned32
_PktcEUERSTNfBCallPermSeqTimer3_Object = MibTableColumn
pktcEUERSTNfBCallPermSeqTimer3 = _PktcEUERSTNfBCallPermSeqTimer3_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 10),
    _PktcEUERSTNfBCallPermSeqTimer3_Type()
)
pktcEUERSTNfBCallPermSeqTimer3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallPermSeqTimer3.setStatus("current")
_PktcEUERSTNfBCallLORTimer_Type = Unsigned32
_PktcEUERSTNfBCallLORTimer_Object = MibTableColumn
pktcEUERSTNfBCallLORTimer = _PktcEUERSTNfBCallLORTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 11),
    _PktcEUERSTNfBCallLORTimer_Type()
)
pktcEUERSTNfBCallLORTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallLORTimer.setStatus("current")


class _PktcEUERSTNfBCallNEMDSCPValueMedia_Type(Unsigned32):
    """Custom type pktcEUERSTNfBCallNEMDSCPValueMedia based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PktcEUERSTNfBCallNEMDSCPValueMedia_Type.__name__ = "Unsigned32"
_PktcEUERSTNfBCallNEMDSCPValueMedia_Object = MibTableColumn
pktcEUERSTNfBCallNEMDSCPValueMedia = _PktcEUERSTNfBCallNEMDSCPValueMedia_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 12),
    _PktcEUERSTNfBCallNEMDSCPValueMedia_Type()
)
pktcEUERSTNfBCallNEMDSCPValueMedia.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallNEMDSCPValueMedia.setStatus("current")


class _PktcEUERSTNfBCallNEMDSCPValueSig_Type(Unsigned32):
    """Custom type pktcEUERSTNfBCallNEMDSCPValueSig based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PktcEUERSTNfBCallNEMDSCPValueSig_Type.__name__ = "Unsigned32"
_PktcEUERSTNfBCallNEMDSCPValueSig_Object = MibTableColumn
pktcEUERSTNfBCallNEMDSCPValueSig = _PktcEUERSTNfBCallNEMDSCPValueSig_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 13),
    _PktcEUERSTNfBCallNEMDSCPValueSig_Type()
)
pktcEUERSTNfBCallNEMDSCPValueSig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallNEMDSCPValueSig.setStatus("current")
_PktcEUERSTNfBCallStatus_Type = RowStatus
_PktcEUERSTNfBCallStatus_Object = MibTableColumn
pktcEUERSTNfBCallStatus = _PktcEUERSTNfBCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 14),
    _PktcEUERSTNfBCallStatus_Type()
)
pktcEUERSTNfBCallStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallStatus.setStatus("current")
_PktcEUERSTNFBCallOrigModLongIntDig_Type = Unsigned32
_PktcEUERSTNFBCallOrigModLongIntDig_Object = MibTableColumn
pktcEUERSTNFBCallOrigModLongIntDig = _PktcEUERSTNFBCallOrigModLongIntDig_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 15),
    _PktcEUERSTNFBCallOrigModLongIntDig_Type()
)
pktcEUERSTNFBCallOrigModLongIntDig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNFBCallOrigModLongIntDig.setStatus("current")
_PktcEUERSTNfBCallPermSeqTone4_Type = Uri
_PktcEUERSTNfBCallPermSeqTone4_Object = MibTableColumn
pktcEUERSTNfBCallPermSeqTone4 = _PktcEUERSTNfBCallPermSeqTone4_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 16),
    _PktcEUERSTNfBCallPermSeqTone4_Type()
)
pktcEUERSTNfBCallPermSeqTone4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallPermSeqTone4.setStatus("current")
_PktcEUERSTNfBCallPermSeqTimer4_Type = Unsigned32
_PktcEUERSTNfBCallPermSeqTimer4_Object = MibTableColumn
pktcEUERSTNfBCallPermSeqTimer4 = _PktcEUERSTNfBCallPermSeqTimer4_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 17),
    _PktcEUERSTNfBCallPermSeqTimer4_Type()
)
pktcEUERSTNfBCallPermSeqTimer4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallPermSeqTimer4.setStatus("current")


class _PktcEUERSTNfBCallOverrideNotifyRejected_Type(TruthValue):
    """Custom type pktcEUERSTNfBCallOverrideNotifyRejected based on TruthValue"""
    defaultValue = 2


_PktcEUERSTNfBCallOverrideNotifyRejected_Type.__name__ = "TruthValue"
_PktcEUERSTNfBCallOverrideNotifyRejected_Object = MibTableColumn
pktcEUERSTNfBCallOverrideNotifyRejected = _PktcEUERSTNfBCallOverrideNotifyRejected_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 18),
    _PktcEUERSTNfBCallOverrideNotifyRejected_Type()
)
pktcEUERSTNfBCallOverrideNotifyRejected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallOverrideNotifyRejected.setStatus("current")
_PktcEUERSTAncFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTAncFeat = _PktcEUERSTAncFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2)
)
_PktcEUERSTAncTable_Object = MibTable
pktcEUERSTAncTable = _PktcEUERSTAncTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTAncTable.setStatus("current")
_PktcEUERSTAncEntry_Object = MibTableRow
pktcEUERSTAncEntry = _PktcEUERSTAncEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 1, 1)
)
pktcEUERSTAncEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTAncIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTAncEntry.setStatus("current")
_PktcEUERSTAncIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTAncIndex_Object = MibTableColumn
pktcEUERSTAncIndex = _PktcEUERSTAncIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 1, 1, 1),
    _PktcEUERSTAncIndex_Type()
)
pktcEUERSTAncIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTAncIndex.setStatus("current")
_PktcEUERSTAncPrefLang_Type = SnmpAdminString
_PktcEUERSTAncPrefLang_Object = MibTableColumn
pktcEUERSTAncPrefLang = _PktcEUERSTAncPrefLang_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 1, 1, 2),
    _PktcEUERSTAncPrefLang_Type()
)
pktcEUERSTAncPrefLang.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTAncPrefLang.setStatus("current")
_PktcEUERSTAncStatus_Type = RowStatus
_PktcEUERSTAncStatus_Object = MibTableColumn
pktcEUERSTAncStatus = _PktcEUERSTAncStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 1, 1, 3),
    _PktcEUERSTAncStatus_Type()
)
pktcEUERSTAncStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTAncStatus.setStatus("current")
_PktcEUERSTNfAncTable_Object = MibTable
pktcEUERSTNfAncTable = _PktcEUERSTNfAncTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfAncTable.setStatus("current")
_PktcEUERSTNfAncEntry_Object = MibTableRow
pktcEUERSTNfAncEntry = _PktcEUERSTNfAncEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 2, 1)
)
pktcEUERSTNfAncEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfAncEntry.setStatus("current")


class _PktcEUERSTNfAncRes_Type(Uri):
    """Custom type pktcEUERSTNfAncRes based on Uri"""
    subtypeSpec = Uri.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_PktcEUERSTNfAncRes_Type.__name__ = "Uri"
_PktcEUERSTNfAncRes_Object = MibTableColumn
pktcEUERSTNfAncRes = _PktcEUERSTNfAncRes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 2, 1, 1),
    _PktcEUERSTNfAncRes_Type()
)
pktcEUERSTNfAncRes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncRes.setStatus("current")
_PktcEUERSTNfAncDomain_Type = SnmpAdminString
_PktcEUERSTNfAncDomain_Object = MibTableColumn
pktcEUERSTNfAncDomain = _PktcEUERSTNfAncDomain_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 2, 1, 2),
    _PktcEUERSTNfAncDomain_Type()
)
pktcEUERSTNfAncDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncDomain.setStatus("current")


class _PktcEUERSTNfAncPath_Type(Uri):
    """Custom type pktcEUERSTNfAncPath based on Uri"""
    subtypeSpec = Uri.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_PktcEUERSTNfAncPath_Type.__name__ = "Uri"
_PktcEUERSTNfAncPath_Object = MibTableColumn
pktcEUERSTNfAncPath = _PktcEUERSTNfAncPath_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 2, 1, 3),
    _PktcEUERSTNfAncPath_Type()
)
pktcEUERSTNfAncPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncPath.setStatus("current")
_PktcEUERSTNfAncMIMEType_Type = SnmpAdminString
_PktcEUERSTNfAncMIMEType_Object = MibTableColumn
pktcEUERSTNfAncMIMEType = _PktcEUERSTNfAncMIMEType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 2, 1, 4),
    _PktcEUERSTNfAncMIMEType_Type()
)
pktcEUERSTNfAncMIMEType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMIMEType.setStatus("current")
_PktcEUERSTNfAncStatus_Type = RowStatus
_PktcEUERSTNfAncStatus_Object = MibTableColumn
pktcEUERSTNfAncStatus = _PktcEUERSTNfAncStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 2, 1, 5),
    _PktcEUERSTNfAncStatus_Type()
)
pktcEUERSTNfAncStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncStatus.setStatus("current")
_PktcEUERSTNfAncMapTable_Object = MibTable
pktcEUERSTNfAncMapTable = _PktcEUERSTNfAncMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMapTable.setStatus("current")
_PktcEUERSTNfAncMapEntry_Object = MibTableRow
pktcEUERSTNfAncMapEntry = _PktcEUERSTNfAncMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 3, 1)
)
pktcEUERSTNfAncMapEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncMapRspCode"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMapEntry.setStatus("current")


class _PktcEUERSTNfAncMapRspCode_Type(Unsigned32):
    """Custom type pktcEUERSTNfAncMapRspCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 603),
    )


_PktcEUERSTNfAncMapRspCode_Type.__name__ = "Unsigned32"
_PktcEUERSTNfAncMapRspCode_Object = MibTableColumn
pktcEUERSTNfAncMapRspCode = _PktcEUERSTNfAncMapRspCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 3, 1, 1),
    _PktcEUERSTNfAncMapRspCode_Type()
)
pktcEUERSTNfAncMapRspCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMapRspCode.setStatus("current")


class _PktcEUERSTNfAncMapURI_Type(Uri):
    """Custom type pktcEUERSTNfAncMapURI based on Uri"""
    subtypeSpec = Uri.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_PktcEUERSTNfAncMapURI_Type.__name__ = "Uri"
_PktcEUERSTNfAncMapURI_Object = MibTableColumn
pktcEUERSTNfAncMapURI = _PktcEUERSTNfAncMapURI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 3, 1, 2),
    _PktcEUERSTNfAncMapURI_Type()
)
pktcEUERSTNfAncMapURI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMapURI.setStatus("current")
_PktcEUERSTNfAncMapStatus_Type = RowStatus
_PktcEUERSTNfAncMapStatus_Object = MibTableColumn
pktcEUERSTNfAncMapStatus = _PktcEUERSTNfAncMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 3, 1, 3),
    _PktcEUERSTNfAncMapStatus_Type()
)
pktcEUERSTNfAncMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMapStatus.setStatus("current")
_PktcEUERSTNfAncMediaMapTable_Object = MibTable
pktcEUERSTNfAncMediaMapTable = _PktcEUERSTNfAncMediaMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMediaMapTable.setStatus("current")
_PktcEUERSTNfAncMediaMapEntry_Object = MibTableRow
pktcEUERSTNfAncMediaMapEntry = _PktcEUERSTNfAncMediaMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 4, 1)
)
pktcEUERSTNfAncMediaMapEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncMediaId"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMediaMapEntry.setStatus("current")


class _PktcEUERSTNfAncMediaId_Type(SnmpAdminString):
    """Custom type pktcEUERSTNfAncMediaId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_PktcEUERSTNfAncMediaId_Type.__name__ = "SnmpAdminString"
_PktcEUERSTNfAncMediaId_Object = MibTableColumn
pktcEUERSTNfAncMediaId = _PktcEUERSTNfAncMediaId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 4, 1, 1),
    _PktcEUERSTNfAncMediaId_Type()
)
pktcEUERSTNfAncMediaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMediaId.setStatus("current")


class _PktcEUERSTNfAncMediaURI_Type(Uri):
    """Custom type pktcEUERSTNfAncMediaURI based on Uri"""
    subtypeSpec = Uri.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_PktcEUERSTNfAncMediaURI_Type.__name__ = "Uri"
_PktcEUERSTNfAncMediaURI_Object = MibTableColumn
pktcEUERSTNfAncMediaURI = _PktcEUERSTNfAncMediaURI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 4, 1, 2),
    _PktcEUERSTNfAncMediaURI_Type()
)
pktcEUERSTNfAncMediaURI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMediaURI.setStatus("current")
_PktcEUERSTNfAncMediaCachMaxAge_Type = Unsigned32
_PktcEUERSTNfAncMediaCachMaxAge_Object = MibTableColumn
pktcEUERSTNfAncMediaCachMaxAge = _PktcEUERSTNfAncMediaCachMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 4, 1, 3),
    _PktcEUERSTNfAncMediaCachMaxAge_Type()
)
pktcEUERSTNfAncMediaCachMaxAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMediaCachMaxAge.setStatus("current")
_PktcEUERSTNfAncMediaStatus_Type = RowStatus
_PktcEUERSTNfAncMediaStatus_Object = MibTableColumn
pktcEUERSTNfAncMediaStatus = _PktcEUERSTNfAncMediaStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 4, 1, 4),
    _PktcEUERSTNfAncMediaStatus_Type()
)
pktcEUERSTNfAncMediaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMediaStatus.setStatus("current")
_PktcEUERSTNfAncLocalMediaTable_Object = MibTable
pktcEUERSTNfAncLocalMediaTable = _PktcEUERSTNfAncLocalMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfAncLocalMediaTable.setStatus("current")
_PktcEUERSTNfAncLocalMediaEntry_Object = MibTableRow
pktcEUERSTNfAncLocalMediaEntry = _PktcEUERSTNfAncLocalMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 5, 1)
)
pktcEUERSTNfAncLocalMediaEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncLclMediaURI"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfAncLocalMediaEntry.setStatus("current")


class _PktcEUERSTNfAncLclMediaURI_Type(Uri):
    """Custom type pktcEUERSTNfAncLclMediaURI based on Uri"""
    subtypeSpec = Uri.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 108),
    )


_PktcEUERSTNfAncLclMediaURI_Type.__name__ = "Uri"
_PktcEUERSTNfAncLclMediaURI_Object = MibTableColumn
pktcEUERSTNfAncLclMediaURI = _PktcEUERSTNfAncLclMediaURI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 5, 1, 1),
    _PktcEUERSTNfAncLclMediaURI_Type()
)
pktcEUERSTNfAncLclMediaURI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncLclMediaURI.setStatus("current")
_PktcEUERSTNfAncLclMediaType_Type = SnmpAdminString
_PktcEUERSTNfAncLclMediaType_Object = MibTableColumn
pktcEUERSTNfAncLclMediaType = _PktcEUERSTNfAncLclMediaType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 5, 1, 2),
    _PktcEUERSTNfAncLclMediaType_Type()
)
pktcEUERSTNfAncLclMediaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncLclMediaType.setStatus("current")
_PktcEUERSTNfAncLclMediaData_Type = SnmpAdminString
_PktcEUERSTNfAncLclMediaData_Object = MibTableColumn
pktcEUERSTNfAncLclMediaData = _PktcEUERSTNfAncLclMediaData_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 5, 1, 3),
    _PktcEUERSTNfAncLclMediaData_Type()
)
pktcEUERSTNfAncLclMediaData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncLclMediaData.setStatus("current")
_PktcEUERSTNfAncLclMediaStatus_Type = RowStatus
_PktcEUERSTNfAncLclMediaStatus_Object = MibTableColumn
pktcEUERSTNfAncLclMediaStatus = _PktcEUERSTNfAncLclMediaStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 5, 1, 4),
    _PktcEUERSTNfAncLclMediaStatus_Type()
)
pktcEUERSTNfAncLclMediaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncLclMediaStatus.setStatus("current")
_PktcEUERSTUEActStatChgFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTUEActStatChgFeat = _PktcEUERSTUEActStatChgFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 3)
)
_PktcEUERSTUEActStatChgTable_Object = MibTable
pktcEUERSTUEActStatChgTable = _PktcEUERSTUEActStatChgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTUEActStatChgTable.setStatus("current")
_PktcEUERSTUEActStatChgEntry_Object = MibTableRow
pktcEUERSTUEActStatChgEntry = _PktcEUERSTUEActStatChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 3, 1, 1)
)
pktcEUERSTUEActStatChgEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTUEActStatChgIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTUEActStatChgEntry.setStatus("current")
_PktcEUERSTUEActStatChgIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTUEActStatChgIndex_Object = MibTableColumn
pktcEUERSTUEActStatChgIndex = _PktcEUERSTUEActStatChgIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 3, 1, 1, 1),
    _PktcEUERSTUEActStatChgIndex_Type()
)
pktcEUERSTUEActStatChgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTUEActStatChgIndex.setStatus("current")
_PktcEUERSTUEActStatChgRegExp_Type = Unsigned32
_PktcEUERSTUEActStatChgRegExp_Object = MibTableColumn
pktcEUERSTUEActStatChgRegExp = _PktcEUERSTUEActStatChgRegExp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 3, 1, 1, 2),
    _PktcEUERSTUEActStatChgRegExp_Type()
)
pktcEUERSTUEActStatChgRegExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTUEActStatChgRegExp.setStatus("current")
_PktcEUERSTUEActStatChgStatus_Type = RowStatus
_PktcEUERSTUEActStatChgStatus_Object = MibTableColumn
pktcEUERSTUEActStatChgStatus = _PktcEUERSTUEActStatChgStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 3, 1, 1, 3),
    _PktcEUERSTUEActStatChgStatus_Type()
)
pktcEUERSTUEActStatChgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTUEActStatChgStatus.setStatus("current")
_PktcEUERSTNoAnsTimeoutFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTNoAnsTimeoutFeat = _PktcEUERSTNoAnsTimeoutFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 4)
)
_PktcEUERSTNoAnsTimeoutTable_Object = MibTable
pktcEUERSTNoAnsTimeoutTable = _PktcEUERSTNoAnsTimeoutTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTNoAnsTimeoutTable.setStatus("current")
_PktcEUERSTNoAnsTimeoutEntry_Object = MibTableRow
pktcEUERSTNoAnsTimeoutEntry = _PktcEUERSTNoAnsTimeoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 4, 1, 1)
)
pktcEUERSTNoAnsTimeoutEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTNoAnsTOIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNoAnsTimeoutEntry.setStatus("current")
_PktcEUERSTNoAnsTOIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTNoAnsTOIndex_Object = MibTableColumn
pktcEUERSTNoAnsTOIndex = _PktcEUERSTNoAnsTOIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 4, 1, 1, 1),
    _PktcEUERSTNoAnsTOIndex_Type()
)
pktcEUERSTNoAnsTOIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTNoAnsTOIndex.setStatus("current")
_PktcEUERSTNoAnsTODuration_Type = Unsigned32
_PktcEUERSTNoAnsTODuration_Object = MibTableColumn
pktcEUERSTNoAnsTODuration = _PktcEUERSTNoAnsTODuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 4, 1, 1, 2),
    _PktcEUERSTNoAnsTODuration_Type()
)
pktcEUERSTNoAnsTODuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNoAnsTODuration.setStatus("current")
_PktcEUERSTNoAnsTOStatus_Type = RowStatus
_PktcEUERSTNoAnsTOStatus_Object = MibTableColumn
pktcEUERSTNoAnsTOStatus = _PktcEUERSTNoAnsTOStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 4, 1, 1, 3),
    _PktcEUERSTNoAnsTOStatus_Type()
)
pktcEUERSTNoAnsTOStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNoAnsTOStatus.setStatus("current")
_PktcEUERSTCallerIdFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTCallerIdFeat = _PktcEUERSTCallerIdFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 5)
)
_PktcEUERSTCIDTable_Object = MibTable
pktcEUERSTCIDTable = _PktcEUERSTCIDTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTCIDTable.setStatus("current")
_PktcEUERSTCIDEntry_Object = MibTableRow
pktcEUERSTCIDEntry = _PktcEUERSTCIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 5, 1, 1)
)
pktcEUERSTCIDEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTCIDEntry.setStatus("current")
_PktcEUERSTCIDIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTCIDIndex_Object = MibTableColumn
pktcEUERSTCIDIndex = _PktcEUERSTCIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 5, 1, 1, 1),
    _PktcEUERSTCIDIndex_Type()
)
pktcEUERSTCIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTCIDIndex.setStatus("current")


class _PktcEUERSTCIDPPS_Type(Integer32):
    """Custom type pktcEUERSTCIDPPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anonymous", 1),
          ("public", 2))
    )


_PktcEUERSTCIDPPS_Type.__name__ = "Integer32"
_PktcEUERSTCIDPPS_Object = MibTableColumn
pktcEUERSTCIDPPS = _PktcEUERSTCIDPPS_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 5, 1, 1, 2),
    _PktcEUERSTCIDPPS_Type()
)
pktcEUERSTCIDPPS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCIDPPS.setStatus("current")
_PktcEUERSTCIDStatus_Type = RowStatus
_PktcEUERSTCIDStatus_Object = MibTableColumn
pktcEUERSTCIDStatus = _PktcEUERSTCIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 5, 1, 1, 3),
    _PktcEUERSTCIDStatus_Type()
)
pktcEUERSTCIDStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCIDStatus.setStatus("current")
_PktcEUERSTCIDDisFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTCIDDisFeat = _PktcEUERSTCIDDisFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6)
)
_PktcEUERSTCIDDisTable_Object = MibTable
pktcEUERSTCIDDisTable = _PktcEUERSTCIDDisTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisTable.setStatus("current")
_PktcEUERSTCIDDisEntry_Object = MibTableRow
pktcEUERSTCIDDisEntry = _PktcEUERSTCIDDisEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 1, 1)
)
pktcEUERSTCIDDisEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDisIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisEntry.setStatus("current")
_PktcEUERSTCIDDisIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTCIDDisIndex_Object = MibTableColumn
pktcEUERSTCIDDisIndex = _PktcEUERSTCIDDisIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 1, 1, 1),
    _PktcEUERSTCIDDisIndex_Type()
)
pktcEUERSTCIDDisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisIndex.setStatus("current")
_PktcEUERSTCIDDisCNDActStat_Type = TruthValue
_PktcEUERSTCIDDisCNDActStat_Object = MibTableColumn
pktcEUERSTCIDDisCNDActStat = _PktcEUERSTCIDDisCNDActStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 1, 1, 2),
    _PktcEUERSTCIDDisCNDActStat_Type()
)
pktcEUERSTCIDDisCNDActStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisCNDActStat.setStatus("current")
_PktcEUERSTCIDDisCNAMDActStat_Type = TruthValue
_PktcEUERSTCIDDisCNAMDActStat_Object = MibTableColumn
pktcEUERSTCIDDisCNAMDActStat = _PktcEUERSTCIDDisCNAMDActStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 1, 1, 3),
    _PktcEUERSTCIDDisCNAMDActStat_Type()
)
pktcEUERSTCIDDisCNAMDActStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisCNAMDActStat.setStatus("current")
_PktcEUERSTCIDDisDefCountry_Type = SnmpAdminString
_PktcEUERSTCIDDisDefCountry_Object = MibTableColumn
pktcEUERSTCIDDisDefCountry = _PktcEUERSTCIDDisDefCountry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 1, 1, 4),
    _PktcEUERSTCIDDisDefCountry_Type()
)
pktcEUERSTCIDDisDefCountry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisDefCountry.setStatus("current")
_PktcEUERSTCIDDisStatus_Type = RowStatus
_PktcEUERSTCIDDisStatus_Object = MibTableColumn
pktcEUERSTCIDDisStatus = _PktcEUERSTCIDDisStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 1, 1, 5),
    _PktcEUERSTCIDDisStatus_Type()
)
pktcEUERSTCIDDisStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisStatus.setStatus("current")


class _PktcEUERSTCIDDisCIDCWActStat_Type(TruthValue):
    """Custom type pktcEUERSTCIDDisCIDCWActStat based on TruthValue"""
    defaultValue = 1


_PktcEUERSTCIDDisCIDCWActStat_Type.__name__ = "TruthValue"
_PktcEUERSTCIDDisCIDCWActStat_Object = MibTableColumn
pktcEUERSTCIDDisCIDCWActStat = _PktcEUERSTCIDDisCIDCWActStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 1, 1, 6),
    _PktcEUERSTCIDDisCIDCWActStat_Type()
)
pktcEUERSTCIDDisCIDCWActStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisCIDCWActStat.setStatus("current")
_PktcEUERSTCIDDisTimeAdj_Type = Integer32
_PktcEUERSTCIDDisTimeAdj_Object = MibScalar
pktcEUERSTCIDDisTimeAdj = _PktcEUERSTCIDDisTimeAdj_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 2),
    _PktcEUERSTCIDDisTimeAdj_Type()
)
pktcEUERSTCIDDisTimeAdj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisTimeAdj.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisTimeAdj.setUnits("minutes")


class _PktcEUERSTCIDDisDSTFlag_Type(TruthValue):
    """Custom type pktcEUERSTCIDDisDSTFlag based on TruthValue"""
    defaultValue = 1


_PktcEUERSTCIDDisDSTFlag_Type.__name__ = "TruthValue"
_PktcEUERSTCIDDisDSTFlag_Object = MibScalar
pktcEUERSTCIDDisDSTFlag = _PktcEUERSTCIDDisDSTFlag_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 3),
    _PktcEUERSTCIDDisDSTFlag_Type()
)
pktcEUERSTCIDDisDSTFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisDSTFlag.setStatus("current")
_PktcEUERSTCIDDisDSTInfo_Type = SnmpAdminString
_PktcEUERSTCIDDisDSTInfo_Object = MibScalar
pktcEUERSTCIDDisDSTInfo = _PktcEUERSTCIDDisDSTInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 4),
    _PktcEUERSTCIDDisDSTInfo_Type()
)
pktcEUERSTCIDDisDSTInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisDSTInfo.setStatus("current")
_PktcEUERSTCIDCallBlkFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTCIDCallBlkFeat = _PktcEUERSTCIDCallBlkFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 7)
)
_PktcEUERSTCallBlkTable_Object = MibTable
pktcEUERSTCallBlkTable = _PktcEUERSTCallBlkTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTCallBlkTable.setStatus("current")
_PktcEUERSTCallBlkEntry_Object = MibTableRow
pktcEUERSTCallBlkEntry = _PktcEUERSTCallBlkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 7, 1, 1)
)
pktcEUERSTCallBlkEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDBlkIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTCallBlkEntry.setStatus("current")
_PktcEUERSTCIDBlkIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTCIDBlkIndex_Object = MibTableColumn
pktcEUERSTCIDBlkIndex = _PktcEUERSTCIDBlkIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 7, 1, 1, 1),
    _PktcEUERSTCIDBlkIndex_Type()
)
pktcEUERSTCIDBlkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTCIDBlkIndex.setStatus("current")
_PktcEUERSTCIDCBlkConfTone_Type = Uri
_PktcEUERSTCIDCBlkConfTone_Object = MibTableColumn
pktcEUERSTCIDCBlkConfTone = _PktcEUERSTCIDCBlkConfTone_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 7, 1, 1, 2),
    _PktcEUERSTCIDCBlkConfTone_Type()
)
pktcEUERSTCIDCBlkConfTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCIDCBlkConfTone.setStatus("current")
_PktcEUERSTCIDCBlkErrTone_Type = Uri
_PktcEUERSTCIDCBlkErrTone_Object = MibTableColumn
pktcEUERSTCIDCBlkErrTone = _PktcEUERSTCIDCBlkErrTone_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 7, 1, 1, 3),
    _PktcEUERSTCIDCBlkErrTone_Type()
)
pktcEUERSTCIDCBlkErrTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCIDCBlkErrTone.setStatus("current")
_PktcEUERSTCIDCBlkStatus_Type = RowStatus
_PktcEUERSTCIDCBlkStatus_Object = MibTableColumn
pktcEUERSTCIDCBlkStatus = _PktcEUERSTCIDCBlkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 7, 1, 1, 4),
    _PktcEUERSTCIDCBlkStatus_Type()
)
pktcEUERSTCIDCBlkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCIDCBlkStatus.setStatus("current")
_PktcEUERSTCIDCallDelFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTCIDCallDelFeat = _PktcEUERSTCIDCallDelFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 8)
)
_PktcEUERSTCallDelTable_Object = MibTable
pktcEUERSTCallDelTable = _PktcEUERSTCallDelTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTCallDelTable.setStatus("current")
_PktcEUERSTCallDelEntry_Object = MibTableRow
pktcEUERSTCallDelEntry = _PktcEUERSTCallDelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 8, 1, 1)
)
pktcEUERSTCallDelEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDelIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTCallDelEntry.setStatus("current")
_PktcEUERSTCIDDelIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTCIDDelIndex_Object = MibTableColumn
pktcEUERSTCIDDelIndex = _PktcEUERSTCIDDelIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 8, 1, 1, 1),
    _PktcEUERSTCIDDelIndex_Type()
)
pktcEUERSTCIDDelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDelIndex.setStatus("current")
_PktcEUERSTCIDDelConfTone_Type = Uri
_PktcEUERSTCIDDelConfTone_Object = MibTableColumn
pktcEUERSTCIDDelConfTone = _PktcEUERSTCIDDelConfTone_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 8, 1, 1, 2),
    _PktcEUERSTCIDDelConfTone_Type()
)
pktcEUERSTCIDDelConfTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDelConfTone.setStatus("current")
_PktcEUERSTCIDDelErrTone_Type = Uri
_PktcEUERSTCIDDelErrTone_Object = MibTableColumn
pktcEUERSTCIDDelErrTone = _PktcEUERSTCIDDelErrTone_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 8, 1, 1, 3),
    _PktcEUERSTCIDDelErrTone_Type()
)
pktcEUERSTCIDDelErrTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDelErrTone.setStatus("current")
_PktcEUERSTCIDDelStatus_Type = RowStatus
_PktcEUERSTCIDDelStatus_Object = MibTableColumn
pktcEUERSTCIDDelStatus = _PktcEUERSTCIDDelStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 8, 1, 1, 4),
    _PktcEUERSTCIDDelStatus_Type()
)
pktcEUERSTCIDDelStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDelStatus.setStatus("current")
_PktcEUERSTCFwdFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTCFwdFeat = _PktcEUERSTCFwdFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9)
)
_PktcEUERSTCallFwdTable_Object = MibTable
pktcEUERSTCallFwdTable = _PktcEUERSTCallFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTCallFwdTable.setStatus("current")
_PktcEUERSTCallFwdEntry_Object = MibTableRow
pktcEUERSTCallFwdEntry = _PktcEUERSTCallFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 1, 1)
)
pktcEUERSTCallFwdEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallFwdIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTCallFwdEntry.setStatus("current")
_PktcEUERSTCallFwdIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTCallFwdIndex_Object = MibTableColumn
pktcEUERSTCallFwdIndex = _PktcEUERSTCallFwdIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 1, 1, 1),
    _PktcEUERSTCallFwdIndex_Type()
)
pktcEUERSTCallFwdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTCallFwdIndex.setStatus("current")
_PktcEUERSTCallFwdRingReminder_Type = TruthValue
_PktcEUERSTCallFwdRingReminder_Object = MibTableColumn
pktcEUERSTCallFwdRingReminder = _PktcEUERSTCallFwdRingReminder_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 1, 1, 2),
    _PktcEUERSTCallFwdRingReminder_Type()
)
pktcEUERSTCallFwdRingReminder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCallFwdRingReminder.setStatus("current")
_PktcEUERSTCallFwdSubDuration_Type = Unsigned32
_PktcEUERSTCallFwdSubDuration_Object = MibTableColumn
pktcEUERSTCallFwdSubDuration = _PktcEUERSTCallFwdSubDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 1, 1, 3),
    _PktcEUERSTCallFwdSubDuration_Type()
)
pktcEUERSTCallFwdSubDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCallFwdSubDuration.setStatus("current")
_PktcEUERSTCallFwdAUID_Type = PktcEUETCRSTAUID
_PktcEUERSTCallFwdAUID_Object = MibTableColumn
pktcEUERSTCallFwdAUID = _PktcEUERSTCallFwdAUID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 1, 1, 4),
    _PktcEUERSTCallFwdAUID_Type()
)
pktcEUERSTCallFwdAUID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCallFwdAUID.setStatus("current")
_PktcEUERSTCallFwdStatus_Type = RowStatus
_PktcEUERSTCallFwdStatus_Object = MibTableColumn
pktcEUERSTCallFwdStatus = _PktcEUERSTCallFwdStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 1, 1, 5),
    _PktcEUERSTCallFwdStatus_Type()
)
pktcEUERSTCallFwdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCallFwdStatus.setStatus("current")
_PktcEUERSTNfCallFwdTable_Object = MibTable
pktcEUERSTNfCallFwdTable = _PktcEUERSTNfCallFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfCallFwdTable.setStatus("current")
_PktcEUERSTNfCallFwdEntry_Object = MibTableRow
pktcEUERSTNfCallFwdEntry = _PktcEUERSTNfCallFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 2, 1)
)
pktcEUERSTNfCallFwdEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfCallFwdEntry.setStatus("current")
_PktcEUERSTNfCallFwdSpDialTone_Type = TruthValue
_PktcEUERSTNfCallFwdSpDialTone_Object = MibTableColumn
pktcEUERSTNfCallFwdSpDialTone = _PktcEUERSTNfCallFwdSpDialTone_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 2, 1, 1),
    _PktcEUERSTNfCallFwdSpDialTone_Type()
)
pktcEUERSTNfCallFwdSpDialTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfCallFwdSpDialTone.setStatus("current")
_PktcEUERSTNfCallFwdStatus_Type = RowStatus
_PktcEUERSTNfCallFwdStatus_Object = MibTableColumn
pktcEUERSTNfCallFwdStatus = _PktcEUERSTNfCallFwdStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 2, 1, 2),
    _PktcEUERSTNfCallFwdStatus_Type()
)
pktcEUERSTNfCallFwdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfCallFwdStatus.setStatus("current")
_PktcEUERSTCallWaitFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTCallWaitFeat = _PktcEUERSTCallWaitFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 10)
)
_PktcEUERSTCallWaitTable_Object = MibTable
pktcEUERSTCallWaitTable = _PktcEUERSTCallWaitTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTCallWaitTable.setStatus("current")
_PktcEUERSTCallWaitEntry_Object = MibTableRow
pktcEUERSTCallWaitEntry = _PktcEUERSTCallWaitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 10, 1, 1)
)
pktcEUERSTCallWaitEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallWaitIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTCallWaitEntry.setStatus("current")
_PktcEUERSTCallWaitIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTCallWaitIndex_Object = MibTableColumn
pktcEUERSTCallWaitIndex = _PktcEUERSTCallWaitIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 10, 1, 1, 1),
    _PktcEUERSTCallWaitIndex_Type()
)
pktcEUERSTCallWaitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTCallWaitIndex.setStatus("current")


class _PktcEUERSTCallWaitCancelEnable_Type(TruthValue):
    """Custom type pktcEUERSTCallWaitCancelEnable based on TruthValue"""
    defaultValue = 1


_PktcEUERSTCallWaitCancelEnable_Type.__name__ = "TruthValue"
_PktcEUERSTCallWaitCancelEnable_Object = MibTableColumn
pktcEUERSTCallWaitCancelEnable = _PktcEUERSTCallWaitCancelEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 10, 1, 1, 2),
    _PktcEUERSTCallWaitCancelEnable_Type()
)
pktcEUERSTCallWaitCancelEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCallWaitCancelEnable.setStatus("current")
_PktcEUERSTCallWaitStatus_Type = RowStatus
_PktcEUERSTCallWaitStatus_Object = MibTableColumn
pktcEUERSTCallWaitStatus = _PktcEUERSTCallWaitStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 10, 1, 1, 3),
    _PktcEUERSTCallWaitStatus_Type()
)
pktcEUERSTCallWaitStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCallWaitStatus.setStatus("current")


class _PktcEUERSTCallWaitDisconnectTiming_Type(Unsigned32):
    """Custom type pktcEUERSTCallWaitDisconnectTiming based on Unsigned32"""
    defaultValue = 10


_PktcEUERSTCallWaitDisconnectTiming_Type.__name__ = "Unsigned32"
_PktcEUERSTCallWaitDisconnectTiming_Object = MibTableColumn
pktcEUERSTCallWaitDisconnectTiming = _PktcEUERSTCallWaitDisconnectTiming_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 10, 1, 1, 4),
    _PktcEUERSTCallWaitDisconnectTiming_Type()
)
pktcEUERSTCallWaitDisconnectTiming.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCallWaitDisconnectTiming.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUERSTCallWaitDisconnectTiming.setUnits("seconds")
_PktcEUERSTCallHoldFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTCallHoldFeat = _PktcEUERSTCallHoldFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 11)
)
_PktcEUERSTCallHoldTable_Object = MibTable
pktcEUERSTCallHoldTable = _PktcEUERSTCallHoldTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 11, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTCallHoldTable.setStatus("current")
_PktcEUERSTCallHoldEntry_Object = MibTableRow
pktcEUERSTCallHoldEntry = _PktcEUERSTCallHoldEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 11, 1, 1)
)
pktcEUERSTCallHoldEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTCHIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTCallHoldEntry.setStatus("current")
_PktcEUERSTCHIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTCHIndex_Object = MibTableColumn
pktcEUERSTCHIndex = _PktcEUERSTCHIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 11, 1, 1, 1),
    _PktcEUERSTCHIndex_Type()
)
pktcEUERSTCHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTCHIndex.setStatus("current")
_PktcEUERSTCHFeatConfirm_Type = Uri
_PktcEUERSTCHFeatConfirm_Object = MibTableColumn
pktcEUERSTCHFeatConfirm = _PktcEUERSTCHFeatConfirm_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 11, 1, 1, 2),
    _PktcEUERSTCHFeatConfirm_Type()
)
pktcEUERSTCHFeatConfirm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCHFeatConfirm.setStatus("current")
_PktcEUERSTCHStatus_Type = RowStatus
_PktcEUERSTCHStatus_Object = MibTableColumn
pktcEUERSTCHStatus = _PktcEUERSTCHStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 11, 1, 1, 3),
    _PktcEUERSTCHStatus_Type()
)
pktcEUERSTCHStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCHStatus.setStatus("current")
_PktcEUERSTCallXfrFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTCallXfrFeat = _PktcEUERSTCallXfrFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 12)
)
_PktcEUERSTCallXfrTable_Object = MibTable
pktcEUERSTCallXfrTable = _PktcEUERSTCallXfrTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTCallXfrTable.setStatus("current")
_PktcEUERSTCallXfrEntry_Object = MibTableRow
pktcEUERSTCallXfrEntry = _PktcEUERSTCallXfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 12, 1, 1)
)
pktcEUERSTCallXfrEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTCXIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTCallXfrEntry.setStatus("current")
_PktcEUERSTCXIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTCXIndex_Object = MibTableColumn
pktcEUERSTCXIndex = _PktcEUERSTCXIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 12, 1, 1, 1),
    _PktcEUERSTCXIndex_Type()
)
pktcEUERSTCXIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTCXIndex.setStatus("current")
_PktcEUERSTCXNtfyTimeout_Type = Unsigned32
_PktcEUERSTCXNtfyTimeout_Object = MibTableColumn
pktcEUERSTCXNtfyTimeout = _PktcEUERSTCXNtfyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 12, 1, 1, 2),
    _PktcEUERSTCXNtfyTimeout_Type()
)
pktcEUERSTCXNtfyTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCXNtfyTimeout.setStatus("current")
_PktcEUERSTCXStatus_Type = RowStatus
_PktcEUERSTCXStatus_Object = MibTableColumn
pktcEUERSTCXStatus = _PktcEUERSTCXStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 12, 1, 1, 3),
    _PktcEUERSTCXStatus_Type()
)
pktcEUERSTCXStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCXStatus.setStatus("current")
_PktcEUERSTCXInDialogRefer_Type = TruthValue
_PktcEUERSTCXInDialogRefer_Object = MibTableColumn
pktcEUERSTCXInDialogRefer = _PktcEUERSTCXInDialogRefer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 12, 1, 1, 4),
    _PktcEUERSTCXInDialogRefer_Type()
)
pktcEUERSTCXInDialogRefer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCXInDialogRefer.setStatus("current")
_PktcEUERSTCXIncomingOnly_Type = TruthValue
_PktcEUERSTCXIncomingOnly_Object = MibTableColumn
pktcEUERSTCXIncomingOnly = _PktcEUERSTCXIncomingOnly_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 12, 1, 1, 5),
    _PktcEUERSTCXIncomingOnly_Type()
)
pktcEUERSTCXIncomingOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTCXIncomingOnly.setStatus("current")
_PktcEUERSTDnDFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTDnDFeat = _PktcEUERSTDnDFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 13)
)
_PktcEUERSTDnDTable_Object = MibTable
pktcEUERSTDnDTable = _PktcEUERSTDnDTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTDnDTable.setStatus("current")
_PktcEUERSTDnDEntry_Object = MibTableRow
pktcEUERSTDnDEntry = _PktcEUERSTDnDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 13, 1, 1)
)
pktcEUERSTDnDEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTDnDIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTDnDEntry.setStatus("current")
_PktcEUERSTDnDIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTDnDIndex_Object = MibTableColumn
pktcEUERSTDnDIndex = _PktcEUERSTDnDIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 13, 1, 1, 1),
    _PktcEUERSTDnDIndex_Type()
)
pktcEUERSTDnDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTDnDIndex.setStatus("current")
_PktcEUERSTDnDActConfirm_Type = Uri
_PktcEUERSTDnDActConfirm_Object = MibTableColumn
pktcEUERSTDnDActConfirm = _PktcEUERSTDnDActConfirm_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 13, 1, 1, 2),
    _PktcEUERSTDnDActConfirm_Type()
)
pktcEUERSTDnDActConfirm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTDnDActConfirm.setStatus("current")
_PktcEUERSTDnDDeActConfirm_Type = Uri
_PktcEUERSTDnDDeActConfirm_Object = MibTableColumn
pktcEUERSTDnDDeActConfirm = _PktcEUERSTDnDDeActConfirm_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 13, 1, 1, 3),
    _PktcEUERSTDnDDeActConfirm_Type()
)
pktcEUERSTDnDDeActConfirm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTDnDDeActConfirm.setStatus("current")
_PktcEUERSTDnDAUID_Type = PktcEUETCRSTAUID
_PktcEUERSTDnDAUID_Object = MibTableColumn
pktcEUERSTDnDAUID = _PktcEUERSTDnDAUID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 13, 1, 1, 4),
    _PktcEUERSTDnDAUID_Type()
)
pktcEUERSTDnDAUID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTDnDAUID.setStatus("current")
_PktcEUERSTDnDStatus_Type = RowStatus
_PktcEUERSTDnDStatus_Object = MibTableColumn
pktcEUERSTDnDStatus = _PktcEUERSTDnDStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 13, 1, 1, 5),
    _PktcEUERSTDnDStatus_Type()
)
pktcEUERSTDnDStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTDnDStatus.setStatus("current")
_PktcEUERSTMWIFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTMWIFeat = _PktcEUERSTMWIFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 14)
)
_PktcEUERSTNfMWITable_Object = MibTable
pktcEUERSTNfMWITable = _PktcEUERSTNfMWITable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 14, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfMWITable.setStatus("current")
_PktcEUERSTNfMWIEntry_Object = MibTableRow
pktcEUERSTNfMWIEntry = _PktcEUERSTNfMWIEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 14, 1, 1)
)
pktcEUERSTNfMWIEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfMWIEntry.setStatus("current")
_PktcEUERSTNfMWISubDuration_Type = Unsigned32
_PktcEUERSTNfMWISubDuration_Object = MibTableColumn
pktcEUERSTNfMWISubDuration = _PktcEUERSTNfMWISubDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 14, 1, 1, 1),
    _PktcEUERSTNfMWISubDuration_Type()
)
pktcEUERSTNfMWISubDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfMWISubDuration.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUERSTNfMWISubDuration.setUnits("seconds")
_PktcEUERSTNfMWIStatus_Type = RowStatus
_PktcEUERSTNfMWIStatus_Object = MibTableColumn
pktcEUERSTNfMWIStatus = _PktcEUERSTNfMWIStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 14, 1, 1, 2),
    _PktcEUERSTNfMWIStatus_Type()
)
pktcEUERSTNfMWIStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfMWIStatus.setStatus("current")
_PktcEUERSTAutoRclFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTAutoRclFeat = _PktcEUERSTAutoRclFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15)
)
_PktcEUERSTAutoRclTable_Object = MibTable
pktcEUERSTAutoRclTable = _PktcEUERSTAutoRclTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTAutoRclTable.setStatus("current")
_PktcEUERSTAutoRclEntry_Object = MibTableRow
pktcEUERSTAutoRclEntry = _PktcEUERSTAutoRclEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1, 1)
)
pktcEUERSTAutoRclEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTARIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTAutoRclEntry.setStatus("current")
_PktcEUERSTARIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTARIndex_Object = MibTableColumn
pktcEUERSTARIndex = _PktcEUERSTARIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1, 1, 1),
    _PktcEUERSTARIndex_Type()
)
pktcEUERSTARIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTARIndex.setStatus("current")


class _PktcEUERSTARTimer_Type(Unsigned32):
    """Custom type pktcEUERSTARTimer based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_PktcEUERSTARTimer_Type.__name__ = "Unsigned32"
_PktcEUERSTARTimer_Object = MibTableColumn
pktcEUERSTARTimer = _PktcEUERSTARTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1, 1, 2),
    _PktcEUERSTARTimer_Type()
)
pktcEUERSTARTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTARTimer.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUERSTARTimer.setUnits("seconds")
_PktcEUERSTARSpRngDuration_Type = Unsigned32
_PktcEUERSTARSpRngDuration_Object = MibTableColumn
pktcEUERSTARSpRngDuration = _PktcEUERSTARSpRngDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1, 1, 3),
    _PktcEUERSTARSpRngDuration_Type()
)
pktcEUERSTARSpRngDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTARSpRngDuration.setStatus("current")
_PktcEUERSTARSpRngRetryTime_Type = Unsigned32
_PktcEUERSTARSpRngRetryTime_Object = MibTableColumn
pktcEUERSTARSpRngRetryTime = _PktcEUERSTARSpRngRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1, 1, 4),
    _PktcEUERSTARSpRngRetryTime_Type()
)
pktcEUERSTARSpRngRetryTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTARSpRngRetryTime.setStatus("current")
_PktcEUERSTARSpRngRetries_Type = Unsigned32
_PktcEUERSTARSpRngRetries_Object = MibTableColumn
pktcEUERSTARSpRngRetries = _PktcEUERSTARSpRngRetries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1, 1, 5),
    _PktcEUERSTARSpRngRetries_Type()
)
pktcEUERSTARSpRngRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTARSpRngRetries.setStatus("current")
_PktcEUERSTARMaxSubSend_Type = Unsigned32
_PktcEUERSTARMaxSubSend_Object = MibTableColumn
pktcEUERSTARMaxSubSend = _PktcEUERSTARMaxSubSend_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1, 1, 6),
    _PktcEUERSTARMaxSubSend_Type()
)
pktcEUERSTARMaxSubSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTARMaxSubSend.setStatus("current")
_PktcEUERSTARMaxSubRec_Type = Unsigned32
_PktcEUERSTARMaxSubRec_Object = MibTableColumn
pktcEUERSTARMaxSubRec = _PktcEUERSTARMaxSubRec_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1, 1, 7),
    _PktcEUERSTARMaxSubRec_Type()
)
pktcEUERSTARMaxSubRec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTARMaxSubRec.setStatus("current")
_PktcEUERSTARStatus_Type = RowStatus
_PktcEUERSTARStatus_Object = MibTableColumn
pktcEUERSTARStatus = _PktcEUERSTARStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1, 1, 8),
    _PktcEUERSTARStatus_Type()
)
pktcEUERSTARStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTARStatus.setStatus("current")
_PktcEUERSTAutoCbFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTAutoCbFeat = _PktcEUERSTAutoCbFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16)
)
_PktcEUERSTAutoCbTable_Object = MibTable
pktcEUERSTAutoCbTable = _PktcEUERSTAutoCbTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTAutoCbTable.setStatus("current")
_PktcEUERSTAutoCbEntry_Object = MibTableRow
pktcEUERSTAutoCbEntry = _PktcEUERSTAutoCbEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1, 1)
)
pktcEUERSTAutoCbEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTACbIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTAutoCbEntry.setStatus("current")
_PktcEUERSTACbIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTACbIndex_Object = MibTableColumn
pktcEUERSTACbIndex = _PktcEUERSTACbIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1, 1, 1),
    _PktcEUERSTACbIndex_Type()
)
pktcEUERSTACbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTACbIndex.setStatus("current")


class _PktcEUERSTACbTimer_Type(Unsigned32):
    """Custom type pktcEUERSTACbTimer based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_PktcEUERSTACbTimer_Type.__name__ = "Unsigned32"
_PktcEUERSTACbTimer_Object = MibTableColumn
pktcEUERSTACbTimer = _PktcEUERSTACbTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1, 1, 2),
    _PktcEUERSTACbTimer_Type()
)
pktcEUERSTACbTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTACbTimer.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUERSTACbTimer.setUnits("seconds")
_PktcEUERSTACbSpRngDuration_Type = Unsigned32
_PktcEUERSTACbSpRngDuration_Object = MibTableColumn
pktcEUERSTACbSpRngDuration = _PktcEUERSTACbSpRngDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1, 1, 3),
    _PktcEUERSTACbSpRngDuration_Type()
)
pktcEUERSTACbSpRngDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTACbSpRngDuration.setStatus("current")
_PktcEUERSTACbSpRngRetryTime_Type = Unsigned32
_PktcEUERSTACbSpRngRetryTime_Object = MibTableColumn
pktcEUERSTACbSpRngRetryTime = _PktcEUERSTACbSpRngRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1, 1, 4),
    _PktcEUERSTACbSpRngRetryTime_Type()
)
pktcEUERSTACbSpRngRetryTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTACbSpRngRetryTime.setStatus("current")
_PktcEUERSTACbSpRngRetries_Type = Unsigned32
_PktcEUERSTACbSpRngRetries_Object = MibTableColumn
pktcEUERSTACbSpRngRetries = _PktcEUERSTACbSpRngRetries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1, 1, 5),
    _PktcEUERSTACbSpRngRetries_Type()
)
pktcEUERSTACbSpRngRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTACbSpRngRetries.setStatus("current")
_PktcEUERSTACbMaxSubSend_Type = Unsigned32
_PktcEUERSTACbMaxSubSend_Object = MibTableColumn
pktcEUERSTACbMaxSubSend = _PktcEUERSTACbMaxSubSend_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1, 1, 6),
    _PktcEUERSTACbMaxSubSend_Type()
)
pktcEUERSTACbMaxSubSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTACbMaxSubSend.setStatus("current")
_PktcEUERSTACbMaxSubRec_Type = Unsigned32
_PktcEUERSTACbMaxSubRec_Object = MibTableColumn
pktcEUERSTACbMaxSubRec = _PktcEUERSTACbMaxSubRec_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1, 1, 7),
    _PktcEUERSTACbMaxSubRec_Type()
)
pktcEUERSTACbMaxSubRec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTACbMaxSubRec.setStatus("current")
_PktcEUERSTACbStatus_Type = RowStatus
_PktcEUERSTACbStatus_Object = MibTableColumn
pktcEUERSTACbStatus = _PktcEUERSTACbStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1, 1, 8),
    _PktcEUERSTACbStatus_Type()
)
pktcEUERSTACbStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTACbStatus.setStatus("current")
_PktcEUERSTBusyLineVFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTBusyLineVFeat = _PktcEUERSTBusyLineVFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 17)
)
_PktcEUERSTNfBusyLineVTable_Object = MibTable
pktcEUERSTNfBusyLineVTable = _PktcEUERSTNfBusyLineVTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 17, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfBusyLineVTable.setStatus("current")
_PktcEUERSTNfBusyLineVEntry_Object = MibTableRow
pktcEUERSTNfBusyLineVEntry = _PktcEUERSTNfBusyLineVEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 17, 1, 1)
)
pktcEUERSTNfBusyLineVEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfBusyLineVEntry.setStatus("current")
_PktcEUERSTNfBLVOperId_Type = SnmpAdminString
_PktcEUERSTNfBLVOperId_Object = MibTableColumn
pktcEUERSTNfBLVOperId = _PktcEUERSTNfBLVOperId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 17, 1, 1, 1),
    _PktcEUERSTNfBLVOperId_Type()
)
pktcEUERSTNfBLVOperId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBLVOperId.setStatus("current")
_PktcEUERSTNfBLVStatus_Type = RowStatus
_PktcEUERSTNfBLVStatus_Object = MibTableColumn
pktcEUERSTNfBLVStatus = _PktcEUERSTNfBLVStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 17, 1, 1, 2),
    _PktcEUERSTNfBLVStatus_Type()
)
pktcEUERSTNfBLVStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfBLVStatus.setStatus("current")
_PktcEUERSTEmSvcFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTEmSvcFeat = _PktcEUERSTEmSvcFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 18)
)
_PktcEUERSTNfEmSvcTable_Object = MibTable
pktcEUERSTNfEmSvcTable = _PktcEUERSTNfEmSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 18, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfEmSvcTable.setStatus("current")
_PktcEUERSTNfEmSvcEntry_Object = MibTableRow
pktcEUERSTNfEmSvcEntry = _PktcEUERSTNfEmSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 18, 1, 1)
)
pktcEUERSTNfEmSvcEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfEmSvcEntry.setStatus("current")


class _PktcEUERSTNfEmSvcNwHoldTimer_Type(Unsigned32):
    """Custom type pktcEUERSTNfEmSvcNwHoldTimer based on Unsigned32"""
    defaultValue = 45


_PktcEUERSTNfEmSvcNwHoldTimer_Type.__name__ = "Unsigned32"
_PktcEUERSTNfEmSvcNwHoldTimer_Object = MibTableColumn
pktcEUERSTNfEmSvcNwHoldTimer = _PktcEUERSTNfEmSvcNwHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 18, 1, 1, 1),
    _PktcEUERSTNfEmSvcNwHoldTimer_Type()
)
pktcEUERSTNfEmSvcNwHoldTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfEmSvcNwHoldTimer.setStatus("current")


class _PktcEUERSTNfEmSvcHowlTimer_Type(Unsigned32):
    """Custom type pktcEUERSTNfEmSvcHowlTimer based on Unsigned32"""
    defaultValue = 3


_PktcEUERSTNfEmSvcHowlTimer_Type.__name__ = "Unsigned32"
_PktcEUERSTNfEmSvcHowlTimer_Object = MibTableColumn
pktcEUERSTNfEmSvcHowlTimer = _PktcEUERSTNfEmSvcHowlTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 18, 1, 1, 2),
    _PktcEUERSTNfEmSvcHowlTimer_Type()
)
pktcEUERSTNfEmSvcHowlTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfEmSvcHowlTimer.setStatus("current")


class _PktcEUERSTNfEmSvcDSCPValMedia_Type(Unsigned32):
    """Custom type pktcEUERSTNfEmSvcDSCPValMedia based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PktcEUERSTNfEmSvcDSCPValMedia_Type.__name__ = "Unsigned32"
_PktcEUERSTNfEmSvcDSCPValMedia_Object = MibTableColumn
pktcEUERSTNfEmSvcDSCPValMedia = _PktcEUERSTNfEmSvcDSCPValMedia_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 18, 1, 1, 3),
    _PktcEUERSTNfEmSvcDSCPValMedia_Type()
)
pktcEUERSTNfEmSvcDSCPValMedia.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfEmSvcDSCPValMedia.setStatus("current")


class _PktcEUERSTNfEmSvcDSCPValSig_Type(Unsigned32):
    """Custom type pktcEUERSTNfEmSvcDSCPValSig based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PktcEUERSTNfEmSvcDSCPValSig_Type.__name__ = "Unsigned32"
_PktcEUERSTNfEmSvcDSCPValSig_Object = MibTableColumn
pktcEUERSTNfEmSvcDSCPValSig = _PktcEUERSTNfEmSvcDSCPValSig_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 18, 1, 1, 4),
    _PktcEUERSTNfEmSvcDSCPValSig_Type()
)
pktcEUERSTNfEmSvcDSCPValSig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfEmSvcDSCPValSig.setStatus("current")
_PktcEUERSTNfEmSvcStatus_Type = RowStatus
_PktcEUERSTNfEmSvcStatus_Object = MibTableColumn
pktcEUERSTNfEmSvcStatus = _PktcEUERSTNfEmSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 18, 1, 1, 5),
    _PktcEUERSTNfEmSvcStatus_Type()
)
pktcEUERSTNfEmSvcStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTNfEmSvcStatus.setStatus("current")
_PktcEUERSTSCFFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTSCFFeat = _PktcEUERSTSCFFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 19)
)
_PktcEUERSTSCFTable_Object = MibTable
pktcEUERSTSCFTable = _PktcEUERSTSCFTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 19, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTSCFTable.setStatus("current")
_PktcEUERSTSCFEntry_Object = MibTableRow
pktcEUERSTSCFEntry = _PktcEUERSTSCFEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 19, 1, 1)
)
pktcEUERSTSCFEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTSCFIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTSCFEntry.setStatus("current")
_PktcEUERSTSCFIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTSCFIndex_Object = MibTableColumn
pktcEUERSTSCFIndex = _PktcEUERSTSCFIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 19, 1, 1, 1),
    _PktcEUERSTSCFIndex_Type()
)
pktcEUERSTSCFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTSCFIndex.setStatus("current")
_PktcEUERSTSCFRingReminder_Type = TruthValue
_PktcEUERSTSCFRingReminder_Object = MibTableColumn
pktcEUERSTSCFRingReminder = _PktcEUERSTSCFRingReminder_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 19, 1, 1, 2),
    _PktcEUERSTSCFRingReminder_Type()
)
pktcEUERSTSCFRingReminder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTSCFRingReminder.setStatus("current")
_PktcEUERSTSCFAUID_Type = PktcEUETCRSTAUID
_PktcEUERSTSCFAUID_Object = MibTableColumn
pktcEUERSTSCFAUID = _PktcEUERSTSCFAUID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 19, 1, 1, 3),
    _PktcEUERSTSCFAUID_Type()
)
pktcEUERSTSCFAUID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTSCFAUID.setStatus("current")
_PktcEUERSTSCFStatus_Type = RowStatus
_PktcEUERSTSCFStatus_Object = MibTableColumn
pktcEUERSTSCFStatus = _PktcEUERSTSCFStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 19, 1, 1, 4),
    _PktcEUERSTSCFStatus_Type()
)
pktcEUERSTSCFStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTSCFStatus.setStatus("current")
_PktcEUERSTHeldMediaFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTHeldMediaFeat = _PktcEUERSTHeldMediaFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 20)
)
_PktcEUERSTHeldMediaTable_Object = MibTable
pktcEUERSTHeldMediaTable = _PktcEUERSTHeldMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 20, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTHeldMediaTable.setStatus("current")
_PktcEUERSTHeldMediaEntry_Object = MibTableRow
pktcEUERSTHeldMediaEntry = _PktcEUERSTHeldMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 20, 1, 1)
)
pktcEUERSTHeldMediaEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTHeldMediaIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTHeldMediaEntry.setStatus("current")
_PktcEUERSTHeldMediaIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTHeldMediaIndex_Object = MibTableColumn
pktcEUERSTHeldMediaIndex = _PktcEUERSTHeldMediaIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 20, 1, 1, 1),
    _PktcEUERSTHeldMediaIndex_Type()
)
pktcEUERSTHeldMediaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTHeldMediaIndex.setStatus("current")
_PktcEUERSTHeldMediaEnabled_Type = TruthValue
_PktcEUERSTHeldMediaEnabled_Object = MibTableColumn
pktcEUERSTHeldMediaEnabled = _PktcEUERSTHeldMediaEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 20, 1, 1, 2),
    _PktcEUERSTHeldMediaEnabled_Type()
)
pktcEUERSTHeldMediaEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTHeldMediaEnabled.setStatus("current")
_PktcEUERSTHeldMediaStatus_Type = RowStatus
_PktcEUERSTHeldMediaStatus_Object = MibTableColumn
pktcEUERSTHeldMediaStatus = _PktcEUERSTHeldMediaStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 20, 1, 1, 3),
    _PktcEUERSTHeldMediaStatus_Type()
)
pktcEUERSTHeldMediaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTHeldMediaStatus.setStatus("current")
_PktcEUERSTSpeedDialLocalMapFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTSpeedDialLocalMapFeat = _PktcEUERSTSpeedDialLocalMapFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 21)
)
_PktcEUERSTSpeedDialLocalMapTable_Object = MibTable
pktcEUERSTSpeedDialLocalMapTable = _PktcEUERSTSpeedDialLocalMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 21, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTSpeedDialLocalMapTable.setStatus("current")
_PktcEUERSTSpeedDialLocalMapEntry_Object = MibTableRow
pktcEUERSTSpeedDialLocalMapEntry = _PktcEUERSTSpeedDialLocalMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 21, 1, 1)
)
pktcEUERSTSpeedDialLocalMapEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTSpeedDialLocalMapIndex"),
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTSpeedDialLocalMapId"),
)
if mibBuilder.loadTexts:
    pktcEUERSTSpeedDialLocalMapEntry.setStatus("current")
_PktcEUERSTSpeedDialLocalMapIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTSpeedDialLocalMapIndex_Object = MibTableColumn
pktcEUERSTSpeedDialLocalMapIndex = _PktcEUERSTSpeedDialLocalMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 21, 1, 1, 1),
    _PktcEUERSTSpeedDialLocalMapIndex_Type()
)
pktcEUERSTSpeedDialLocalMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTSpeedDialLocalMapIndex.setStatus("current")


class _PktcEUERSTSpeedDialLocalMapId_Type(Unsigned32):
    """Custom type pktcEUERSTSpeedDialLocalMapId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PktcEUERSTSpeedDialLocalMapId_Type.__name__ = "Unsigned32"
_PktcEUERSTSpeedDialLocalMapId_Object = MibTableColumn
pktcEUERSTSpeedDialLocalMapId = _PktcEUERSTSpeedDialLocalMapId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 21, 1, 1, 2),
    _PktcEUERSTSpeedDialLocalMapId_Type()
)
pktcEUERSTSpeedDialLocalMapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTSpeedDialLocalMapId.setStatus("current")
_PktcEUERSTSpeedDialLocalMapCode_Type = SnmpAdminString
_PktcEUERSTSpeedDialLocalMapCode_Object = MibTableColumn
pktcEUERSTSpeedDialLocalMapCode = _PktcEUERSTSpeedDialLocalMapCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 21, 1, 1, 3),
    _PktcEUERSTSpeedDialLocalMapCode_Type()
)
pktcEUERSTSpeedDialLocalMapCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTSpeedDialLocalMapCode.setStatus("current")
_PktcEUERSTSpeedDialLocalMapDigitString_Type = SnmpAdminString
_PktcEUERSTSpeedDialLocalMapDigitString_Object = MibTableColumn
pktcEUERSTSpeedDialLocalMapDigitString = _PktcEUERSTSpeedDialLocalMapDigitString_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 21, 1, 1, 4),
    _PktcEUERSTSpeedDialLocalMapDigitString_Type()
)
pktcEUERSTSpeedDialLocalMapDigitString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTSpeedDialLocalMapDigitString.setStatus("current")
_PktcEUERSTSpeedDialLocalMapStatus_Type = RowStatus
_PktcEUERSTSpeedDialLocalMapStatus_Object = MibTableColumn
pktcEUERSTSpeedDialLocalMapStatus = _PktcEUERSTSpeedDialLocalMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 21, 1, 1, 5),
    _PktcEUERSTSpeedDialLocalMapStatus_Type()
)
pktcEUERSTSpeedDialLocalMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTSpeedDialLocalMapStatus.setStatus("current")
_PktcEUERSTHotlineFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTHotlineFeat = _PktcEUERSTHotlineFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 22)
)
_PktcEUERSTHotlineTable_Object = MibTable
pktcEUERSTHotlineTable = _PktcEUERSTHotlineTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 22, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTHotlineTable.setStatus("current")
_PktcEUERSTHotlineEntry_Object = MibTableRow
pktcEUERSTHotlineEntry = _PktcEUERSTHotlineEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 22, 1, 1)
)
pktcEUERSTHotlineEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTHotlineIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTHotlineEntry.setStatus("current")
_PktcEUERSTHotlineIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTHotlineIndex_Object = MibTableColumn
pktcEUERSTHotlineIndex = _PktcEUERSTHotlineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 22, 1, 1, 1),
    _PktcEUERSTHotlineIndex_Type()
)
pktcEUERSTHotlineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTHotlineIndex.setStatus("current")
_PktcEUERSTHotlineDestAddress_Type = SnmpAdminString
_PktcEUERSTHotlineDestAddress_Object = MibTableColumn
pktcEUERSTHotlineDestAddress = _PktcEUERSTHotlineDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 22, 1, 1, 2),
    _PktcEUERSTHotlineDestAddress_Type()
)
pktcEUERSTHotlineDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTHotlineDestAddress.setStatus("current")


class _PktcEUERSTHotlineOffhookTimer_Type(Unsigned32):
    """Custom type pktcEUERSTHotlineOffhookTimer based on Unsigned32"""
    defaultValue = 0


_PktcEUERSTHotlineOffhookTimer_Type.__name__ = "Unsigned32"
_PktcEUERSTHotlineOffhookTimer_Object = MibTableColumn
pktcEUERSTHotlineOffhookTimer = _PktcEUERSTHotlineOffhookTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 22, 1, 1, 3),
    _PktcEUERSTHotlineOffhookTimer_Type()
)
pktcEUERSTHotlineOffhookTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTHotlineOffhookTimer.setStatus("current")
if mibBuilder.loadTexts:
    pktcEUERSTHotlineOffhookTimer.setUnits("seconds")
_PktcEUERSTHotlineStatus_Type = RowStatus
_PktcEUERSTHotlineStatus_Object = MibTableColumn
pktcEUERSTHotlineStatus = _PktcEUERSTHotlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 22, 1, 1, 4),
    _PktcEUERSTHotlineStatus_Type()
)
pktcEUERSTHotlineStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTHotlineStatus.setStatus("current")
_PktcEUERST3WCallfeat_ObjectIdentity = ObjectIdentity
pktcEUERST3WCallfeat = _PktcEUERST3WCallfeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 23)
)
_PktcEUERST3WCallTable_Object = MibTable
pktcEUERST3WCallTable = _PktcEUERST3WCallTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 23, 1)
)
if mibBuilder.loadTexts:
    pktcEUERST3WCallTable.setStatus("current")
_PktcEUERST3WCallEntry_Object = MibTableRow
pktcEUERST3WCallEntry = _PktcEUERST3WCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 23, 1, 1)
)
pktcEUERST3WCallEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallWaitIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERST3WCallEntry.setStatus("current")
_PktcEUERST3WCallIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERST3WCallIndex_Object = MibTableColumn
pktcEUERST3WCallIndex = _PktcEUERST3WCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 23, 1, 1, 1),
    _PktcEUERST3WCallIndex_Type()
)
pktcEUERST3WCallIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERST3WCallIndex.setStatus("current")


class _PktcEUERST3WCallDisconnectTiming_Type(Unsigned32):
    """Custom type pktcEUERST3WCallDisconnectTiming based on Unsigned32"""
    defaultValue = 10


_PktcEUERST3WCallDisconnectTiming_Type.__name__ = "Unsigned32"
_PktcEUERST3WCallDisconnectTiming_Object = MibTableColumn
pktcEUERST3WCallDisconnectTiming = _PktcEUERST3WCallDisconnectTiming_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 23, 1, 1, 2),
    _PktcEUERST3WCallDisconnectTiming_Type()
)
pktcEUERST3WCallDisconnectTiming.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERST3WCallDisconnectTiming.setStatus("current")
_PktcEUERST3WCallStatus_Type = RowStatus
_PktcEUERST3WCallStatus_Object = MibTableColumn
pktcEUERST3WCallStatus = _PktcEUERST3WCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 23, 1, 1, 3),
    _PktcEUERST3WCallStatus_Type()
)
pktcEUERST3WCallStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERST3WCallStatus.setStatus("current")
_PktcEUERSTConformance_ObjectIdentity = ObjectIdentity
pktcEUERSTConformance = _PktcEUERSTConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2)
)
_PktcEUERSTCompliances_ObjectIdentity = ObjectIdentity
pktcEUERSTCompliances = _PktcEUERSTCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 1)
)
_PktcEUERSTGroups_ObjectIdentity = ObjectIdentity
pktcEUERSTGroups = _PktcEUERSTGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2)
)

# Managed Objects groups

pktcEUERSTProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 1)
)
pktcEUERSTProfileGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTProfileVersion"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTKeepAliveSetting"))
)
if mibBuilder.loadTexts:
    pktcEUERSTProfileGroup.setStatus("current")

pktcEUERSTBasicCallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 2)
)
pktcEUERSTBasicCallGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTBCallPrefCodecList"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTBCallStatus"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallByeDelay"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallOrigDTTimer"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallTermOHErrSig"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallTermErrSigTimer"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallPermSeqTone1"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallPermSeqTimer1"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallPermSeqTone2"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallPermSeqTimer2"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallPermSeqTone3"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallPermSeqTimer3"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallLORTimer"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallNEMDSCPValueMedia"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallNEMDSCPValueSig"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallStatus"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNFBCallOrigModLongIntDig"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallPermSeqTone4"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallPermSeqTimer4"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallOverrideNotifyRejected"))
)
if mibBuilder.loadTexts:
    pktcEUERSTBasicCallGroup.setStatus("current")

pktcEUERSTAncGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 3)
)
pktcEUERSTAncGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAncPrefLang"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAncStatus"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncRes"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncDomain"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncPath"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncMIMEType"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncStatus"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncMapURI"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncMapStatus"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncMediaURI"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncMediaCachMaxAge"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncMediaStatus"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncLclMediaData"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncLclMediaType"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncLclMediaStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTAncGroup.setStatus("current")

pktcEUERSTUEStGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 4)
)
pktcEUERSTUEStGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTUEActStatChgRegExp"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTUEActStatChgStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTUEStGroup.setStatus("current")

pktcEUERSTNoAnsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 5)
)
pktcEUERSTNoAnsGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNoAnsTODuration"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNoAnsTOStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTNoAnsGroup.setStatus("current")

pktcEUERSTCallerIDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 6)
)
pktcEUERSTCallerIDGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDPPS"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDStatus"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDisTimeAdj"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDisDSTFlag"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDisDSTInfo"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDisCNDActStat"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDisCNAMDActStat"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDisDefCountry"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDisStatus"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDisCIDCWActStat"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDCBlkConfTone"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDCBlkErrTone"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDCBlkStatus"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDelConfTone"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDelErrTone"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDelStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTCallerIDGroup.setStatus("current")

pktcEUERSTCallFwdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 7)
)
pktcEUERSTCallFwdGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallFwdRingReminder"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallFwdSubDuration"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallFwdAUID"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallFwdStatus"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfCallFwdSpDialTone"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfCallFwdStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTCallFwdGroup.setStatus("current")

pktcEUERSTCallHoldGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 8)
)
pktcEUERSTCallHoldGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCHFeatConfirm"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCHStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTCallHoldGroup.setStatus("current")

pktcEUERSTCallTransGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 9)
)
pktcEUERSTCallTransGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCXNtfyTimeout"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCXStatus"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCXInDialogRefer"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCXIncomingOnly"))
)
if mibBuilder.loadTexts:
    pktcEUERSTCallTransGroup.setStatus("current")

pktcEUERSTDNDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 10)
)
pktcEUERSTDNDGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDnDActConfirm"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDnDDeActConfirm"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDnDAUID"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDnDStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTDNDGroup.setStatus("current")

pktcEUERSTMWIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 11)
)
pktcEUERSTMWIGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfMWISubDuration"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfMWIStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTMWIGroup.setStatus("current")

pktcEUERSTAutoRecallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 13)
)
pktcEUERSTAutoRecallGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTARTimer"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTARSpRngDuration"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTARSpRngRetryTime"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTARSpRngRetries"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTARMaxSubSend"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTARMaxSubRec"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTARStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTAutoRecallGroup.setStatus("current")

pktcEUERSTAutoCallbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 14)
)
pktcEUERSTAutoCallbackGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTACbTimer"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTACbSpRngDuration"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTACbSpRngRetryTime"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTACbSpRngRetries"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTACbMaxSubSend"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTACbMaxSubRec"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTACbStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTAutoCallbackGroup.setStatus("current")

pktcEUERSTBusyLineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 15)
)
pktcEUERSTBusyLineGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBLVOperId"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBLVStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTBusyLineGroup.setStatus("current")

pktcEUERSTEmerSvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 16)
)
pktcEUERSTEmerSvcGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfEmSvcNwHoldTimer"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfEmSvcHowlTimer"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfEmSvcDSCPValMedia"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfEmSvcDSCPValSig"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfEmSvcStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTEmerSvcGroup.setStatus("current")

pktcEUERSTDigitMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 17)
)
pktcEUERSTDigitMapGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDMValue"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDMStatus"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDigitMapVariableName"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDigitMapVariableValue"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDigitMapVariableStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTDigitMapGroup.setStatus("current")

pktcEUERSTAppProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 18)
)
pktcEUERSTAppProfileGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppFeatID"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppFeatIndexRef"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppAdminStat"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppAdminStatInfo"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppOperStat"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppOperStatInfo"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTAppProfileGroup.setStatus("current")

pktcEUERSTSCFProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 19)
)
pktcEUERSTSCFProfileGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTSCFRingReminder"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTSCFAUID"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTSCFStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTSCFProfileGroup.setStatus("current")

pktcEUERSTHeldMediaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 20)
)
pktcEUERSTHeldMediaGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTHeldMediaEnabled"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTHeldMediaStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTHeldMediaGroup.setStatus("current")

pktcEUERSTSpeedDialLocalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 21)
)
pktcEUERSTSpeedDialLocalGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTSpeedDialLocalMapCode"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTSpeedDialLocalMapDigitString"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTSpeedDialLocalMapStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTSpeedDialLocalGroup.setStatus("current")

pktcEUERSTHotlineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 22)
)
pktcEUERSTHotlineGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTHotlineDestAddress"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTHotlineOffhookTimer"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTHotlineStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTHotlineGroup.setStatus("current")

pktcEUERSTCallWaitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 23)
)
pktcEUERSTCallWaitGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallWaitCancelEnable"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallWaitStatus"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallWaitDisconnectTiming"))
)
if mibBuilder.loadTexts:
    pktcEUERSTCallWaitGroup.setStatus("current")

pktcEUERST3WCallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 24)
)
pktcEUERST3WCallGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERST3WCallDisconnectTiming"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERST3WCallStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERST3WCallGroup.setStatus("current")

pktcEUERSTDeprecated = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 25)
)
pktcEUERSTDeprecated.setObjects(
    ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTKeepAlive")
)
if mibBuilder.loadTexts:
    pktcEUERSTDeprecated.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcEUERSTCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 1, 1)
)
pktcEUERSTCompliance.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTProfileGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTBasicCallGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTUEStGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNoAnsGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallerIDGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallFwdGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallHoldGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallTransGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDNDGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTMWIGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAutoRecallGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAutoCallbackGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTBusyLineGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTEmerSvcGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDigitMapGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppProfileGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTSCFProfileGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTHeldMediaGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTHotlineGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallWaitGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERST3WCallGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAncGroup"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTSpeedDialLocalGroup"),
        ("PKTC-IETF-SIG-MIB", "pktcSigDeviceGroup"))
)
if mibBuilder.loadTexts:
    pktcEUERSTCompliance.setStatus(
        "current"
    )

pktcEUERSTDeprecatedCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 1, 2)
)
pktcEUERSTDeprecatedCompliance.setObjects(
    ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDeprecated")
)
if mibBuilder.loadTexts:
    pktcEUERSTDeprecatedCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CL-PKTC-EUE-RST-MIB",
    **{"PktcRSTTCFeatID": PktcRSTTCFeatID,
       "PktcEUETCRSTAppFeatIndexType": PktcEUETCRSTAppFeatIndexType,
       "PktcEUETCRSTAUID": PktcEUETCRSTAUID,
       "pktcEUERSTMIB": pktcEUERSTMIB,
       "pktcEUERSTNotifications": pktcEUERSTNotifications,
       "pktcEUERSTObjects": pktcEUERSTObjects,
       "pktcEUERSTProfile": pktcEUERSTProfile,
       "pktcEUERSTProfileVersion": pktcEUERSTProfileVersion,
       "pktcEUERSTAppProfileToFeatTable": pktcEUERSTAppProfileToFeatTable,
       "pktcEUERSTAppProfileToFeatEntry": pktcEUERSTAppProfileToFeatEntry,
       "pktcEUERSTAppProfileIndex": pktcEUERSTAppProfileIndex,
       "pktcEUERSTAppFeatIndex": pktcEUERSTAppFeatIndex,
       "pktcEUERSTAppFeatID": pktcEUERSTAppFeatID,
       "pktcEUERSTAppFeatIndexRef": pktcEUERSTAppFeatIndexRef,
       "pktcEUERSTAppAdminStat": pktcEUERSTAppAdminStat,
       "pktcEUERSTAppAdminStatInfo": pktcEUERSTAppAdminStatInfo,
       "pktcEUERSTAppOperStat": pktcEUERSTAppOperStat,
       "pktcEUERSTAppOperStatInfo": pktcEUERSTAppOperStatInfo,
       "pktcEUERSTAppStatus": pktcEUERSTAppStatus,
       "pktcEUERSTDigitMapFeat": pktcEUERSTDigitMapFeat,
       "pktcEUERSTDigitMapProfileTable": pktcEUERSTDigitMapProfileTable,
       "pktcEUERSTDigitMapProfileEntry": pktcEUERSTDigitMapProfileEntry,
       "pktcEUERSTDMIndex": pktcEUERSTDMIndex,
       "pktcEUERSTDMValue": pktcEUERSTDMValue,
       "pktcEUERSTDMStatus": pktcEUERSTDMStatus,
       "pktcEUERSTDigitMapVariableTable": pktcEUERSTDigitMapVariableTable,
       "pktcEUERSTDigitMapVariableEntry": pktcEUERSTDigitMapVariableEntry,
       "pktcEUERSTDigitMapVariableIndex": pktcEUERSTDigitMapVariableIndex,
       "pktcEUERSTDigitMapVariableId": pktcEUERSTDigitMapVariableId,
       "pktcEUERSTDigitMapVariableName": pktcEUERSTDigitMapVariableName,
       "pktcEUERSTDigitMapVariableValue": pktcEUERSTDigitMapVariableValue,
       "pktcEUERSTDigitMapVariableStatus": pktcEUERSTDigitMapVariableStatus,
       "pktcEUERSTKeepAlive": pktcEUERSTKeepAlive,
       "pktcEUERSTKeepAliveSetting": pktcEUERSTKeepAliveSetting,
       "pktcEUERSTFeatures": pktcEUERSTFeatures,
       "pktcEUERSTBasicCallFeat": pktcEUERSTBasicCallFeat,
       "pktcEUERSTBasicCallTable": pktcEUERSTBasicCallTable,
       "pktcEUERSTBasicCallEntry": pktcEUERSTBasicCallEntry,
       "pktcEUERSTBCallIndex": pktcEUERSTBCallIndex,
       "pktcEUERSTBCallPrefCodecList": pktcEUERSTBCallPrefCodecList,
       "pktcEUERSTBCallStatus": pktcEUERSTBCallStatus,
       "pktcEUERSTNfBasicCallTable": pktcEUERSTNfBasicCallTable,
       "pktcEUERSTNfBasicCallEntry": pktcEUERSTNfBasicCallEntry,
       "pktcEUERSTNfBCallByeDelay": pktcEUERSTNfBCallByeDelay,
       "pktcEUERSTNfBCallOrigDTTimer": pktcEUERSTNfBCallOrigDTTimer,
       "pktcEUERSTNfBCallTermOHErrSig": pktcEUERSTNfBCallTermOHErrSig,
       "pktcEUERSTNfBCallTermErrSigTimer": pktcEUERSTNfBCallTermErrSigTimer,
       "pktcEUERSTNfBCallPermSeqTone1": pktcEUERSTNfBCallPermSeqTone1,
       "pktcEUERSTNfBCallPermSeqTimer1": pktcEUERSTNfBCallPermSeqTimer1,
       "pktcEUERSTNfBCallPermSeqTone2": pktcEUERSTNfBCallPermSeqTone2,
       "pktcEUERSTNfBCallPermSeqTimer2": pktcEUERSTNfBCallPermSeqTimer2,
       "pktcEUERSTNfBCallPermSeqTone3": pktcEUERSTNfBCallPermSeqTone3,
       "pktcEUERSTNfBCallPermSeqTimer3": pktcEUERSTNfBCallPermSeqTimer3,
       "pktcEUERSTNfBCallLORTimer": pktcEUERSTNfBCallLORTimer,
       "pktcEUERSTNfBCallNEMDSCPValueMedia": pktcEUERSTNfBCallNEMDSCPValueMedia,
       "pktcEUERSTNfBCallNEMDSCPValueSig": pktcEUERSTNfBCallNEMDSCPValueSig,
       "pktcEUERSTNfBCallStatus": pktcEUERSTNfBCallStatus,
       "pktcEUERSTNFBCallOrigModLongIntDig": pktcEUERSTNFBCallOrigModLongIntDig,
       "pktcEUERSTNfBCallPermSeqTone4": pktcEUERSTNfBCallPermSeqTone4,
       "pktcEUERSTNfBCallPermSeqTimer4": pktcEUERSTNfBCallPermSeqTimer4,
       "pktcEUERSTNfBCallOverrideNotifyRejected": pktcEUERSTNfBCallOverrideNotifyRejected,
       "pktcEUERSTAncFeat": pktcEUERSTAncFeat,
       "pktcEUERSTAncTable": pktcEUERSTAncTable,
       "pktcEUERSTAncEntry": pktcEUERSTAncEntry,
       "pktcEUERSTAncIndex": pktcEUERSTAncIndex,
       "pktcEUERSTAncPrefLang": pktcEUERSTAncPrefLang,
       "pktcEUERSTAncStatus": pktcEUERSTAncStatus,
       "pktcEUERSTNfAncTable": pktcEUERSTNfAncTable,
       "pktcEUERSTNfAncEntry": pktcEUERSTNfAncEntry,
       "pktcEUERSTNfAncRes": pktcEUERSTNfAncRes,
       "pktcEUERSTNfAncDomain": pktcEUERSTNfAncDomain,
       "pktcEUERSTNfAncPath": pktcEUERSTNfAncPath,
       "pktcEUERSTNfAncMIMEType": pktcEUERSTNfAncMIMEType,
       "pktcEUERSTNfAncStatus": pktcEUERSTNfAncStatus,
       "pktcEUERSTNfAncMapTable": pktcEUERSTNfAncMapTable,
       "pktcEUERSTNfAncMapEntry": pktcEUERSTNfAncMapEntry,
       "pktcEUERSTNfAncMapRspCode": pktcEUERSTNfAncMapRspCode,
       "pktcEUERSTNfAncMapURI": pktcEUERSTNfAncMapURI,
       "pktcEUERSTNfAncMapStatus": pktcEUERSTNfAncMapStatus,
       "pktcEUERSTNfAncMediaMapTable": pktcEUERSTNfAncMediaMapTable,
       "pktcEUERSTNfAncMediaMapEntry": pktcEUERSTNfAncMediaMapEntry,
       "pktcEUERSTNfAncMediaId": pktcEUERSTNfAncMediaId,
       "pktcEUERSTNfAncMediaURI": pktcEUERSTNfAncMediaURI,
       "pktcEUERSTNfAncMediaCachMaxAge": pktcEUERSTNfAncMediaCachMaxAge,
       "pktcEUERSTNfAncMediaStatus": pktcEUERSTNfAncMediaStatus,
       "pktcEUERSTNfAncLocalMediaTable": pktcEUERSTNfAncLocalMediaTable,
       "pktcEUERSTNfAncLocalMediaEntry": pktcEUERSTNfAncLocalMediaEntry,
       "pktcEUERSTNfAncLclMediaURI": pktcEUERSTNfAncLclMediaURI,
       "pktcEUERSTNfAncLclMediaType": pktcEUERSTNfAncLclMediaType,
       "pktcEUERSTNfAncLclMediaData": pktcEUERSTNfAncLclMediaData,
       "pktcEUERSTNfAncLclMediaStatus": pktcEUERSTNfAncLclMediaStatus,
       "pktcEUERSTUEActStatChgFeat": pktcEUERSTUEActStatChgFeat,
       "pktcEUERSTUEActStatChgTable": pktcEUERSTUEActStatChgTable,
       "pktcEUERSTUEActStatChgEntry": pktcEUERSTUEActStatChgEntry,
       "pktcEUERSTUEActStatChgIndex": pktcEUERSTUEActStatChgIndex,
       "pktcEUERSTUEActStatChgRegExp": pktcEUERSTUEActStatChgRegExp,
       "pktcEUERSTUEActStatChgStatus": pktcEUERSTUEActStatChgStatus,
       "pktcEUERSTNoAnsTimeoutFeat": pktcEUERSTNoAnsTimeoutFeat,
       "pktcEUERSTNoAnsTimeoutTable": pktcEUERSTNoAnsTimeoutTable,
       "pktcEUERSTNoAnsTimeoutEntry": pktcEUERSTNoAnsTimeoutEntry,
       "pktcEUERSTNoAnsTOIndex": pktcEUERSTNoAnsTOIndex,
       "pktcEUERSTNoAnsTODuration": pktcEUERSTNoAnsTODuration,
       "pktcEUERSTNoAnsTOStatus": pktcEUERSTNoAnsTOStatus,
       "pktcEUERSTCallerIdFeat": pktcEUERSTCallerIdFeat,
       "pktcEUERSTCIDTable": pktcEUERSTCIDTable,
       "pktcEUERSTCIDEntry": pktcEUERSTCIDEntry,
       "pktcEUERSTCIDIndex": pktcEUERSTCIDIndex,
       "pktcEUERSTCIDPPS": pktcEUERSTCIDPPS,
       "pktcEUERSTCIDStatus": pktcEUERSTCIDStatus,
       "pktcEUERSTCIDDisFeat": pktcEUERSTCIDDisFeat,
       "pktcEUERSTCIDDisTable": pktcEUERSTCIDDisTable,
       "pktcEUERSTCIDDisEntry": pktcEUERSTCIDDisEntry,
       "pktcEUERSTCIDDisIndex": pktcEUERSTCIDDisIndex,
       "pktcEUERSTCIDDisCNDActStat": pktcEUERSTCIDDisCNDActStat,
       "pktcEUERSTCIDDisCNAMDActStat": pktcEUERSTCIDDisCNAMDActStat,
       "pktcEUERSTCIDDisDefCountry": pktcEUERSTCIDDisDefCountry,
       "pktcEUERSTCIDDisStatus": pktcEUERSTCIDDisStatus,
       "pktcEUERSTCIDDisCIDCWActStat": pktcEUERSTCIDDisCIDCWActStat,
       "pktcEUERSTCIDDisTimeAdj": pktcEUERSTCIDDisTimeAdj,
       "pktcEUERSTCIDDisDSTFlag": pktcEUERSTCIDDisDSTFlag,
       "pktcEUERSTCIDDisDSTInfo": pktcEUERSTCIDDisDSTInfo,
       "pktcEUERSTCIDCallBlkFeat": pktcEUERSTCIDCallBlkFeat,
       "pktcEUERSTCallBlkTable": pktcEUERSTCallBlkTable,
       "pktcEUERSTCallBlkEntry": pktcEUERSTCallBlkEntry,
       "pktcEUERSTCIDBlkIndex": pktcEUERSTCIDBlkIndex,
       "pktcEUERSTCIDCBlkConfTone": pktcEUERSTCIDCBlkConfTone,
       "pktcEUERSTCIDCBlkErrTone": pktcEUERSTCIDCBlkErrTone,
       "pktcEUERSTCIDCBlkStatus": pktcEUERSTCIDCBlkStatus,
       "pktcEUERSTCIDCallDelFeat": pktcEUERSTCIDCallDelFeat,
       "pktcEUERSTCallDelTable": pktcEUERSTCallDelTable,
       "pktcEUERSTCallDelEntry": pktcEUERSTCallDelEntry,
       "pktcEUERSTCIDDelIndex": pktcEUERSTCIDDelIndex,
       "pktcEUERSTCIDDelConfTone": pktcEUERSTCIDDelConfTone,
       "pktcEUERSTCIDDelErrTone": pktcEUERSTCIDDelErrTone,
       "pktcEUERSTCIDDelStatus": pktcEUERSTCIDDelStatus,
       "pktcEUERSTCFwdFeat": pktcEUERSTCFwdFeat,
       "pktcEUERSTCallFwdTable": pktcEUERSTCallFwdTable,
       "pktcEUERSTCallFwdEntry": pktcEUERSTCallFwdEntry,
       "pktcEUERSTCallFwdIndex": pktcEUERSTCallFwdIndex,
       "pktcEUERSTCallFwdRingReminder": pktcEUERSTCallFwdRingReminder,
       "pktcEUERSTCallFwdSubDuration": pktcEUERSTCallFwdSubDuration,
       "pktcEUERSTCallFwdAUID": pktcEUERSTCallFwdAUID,
       "pktcEUERSTCallFwdStatus": pktcEUERSTCallFwdStatus,
       "pktcEUERSTNfCallFwdTable": pktcEUERSTNfCallFwdTable,
       "pktcEUERSTNfCallFwdEntry": pktcEUERSTNfCallFwdEntry,
       "pktcEUERSTNfCallFwdSpDialTone": pktcEUERSTNfCallFwdSpDialTone,
       "pktcEUERSTNfCallFwdStatus": pktcEUERSTNfCallFwdStatus,
       "pktcEUERSTCallWaitFeat": pktcEUERSTCallWaitFeat,
       "pktcEUERSTCallWaitTable": pktcEUERSTCallWaitTable,
       "pktcEUERSTCallWaitEntry": pktcEUERSTCallWaitEntry,
       "pktcEUERSTCallWaitIndex": pktcEUERSTCallWaitIndex,
       "pktcEUERSTCallWaitCancelEnable": pktcEUERSTCallWaitCancelEnable,
       "pktcEUERSTCallWaitStatus": pktcEUERSTCallWaitStatus,
       "pktcEUERSTCallWaitDisconnectTiming": pktcEUERSTCallWaitDisconnectTiming,
       "pktcEUERSTCallHoldFeat": pktcEUERSTCallHoldFeat,
       "pktcEUERSTCallHoldTable": pktcEUERSTCallHoldTable,
       "pktcEUERSTCallHoldEntry": pktcEUERSTCallHoldEntry,
       "pktcEUERSTCHIndex": pktcEUERSTCHIndex,
       "pktcEUERSTCHFeatConfirm": pktcEUERSTCHFeatConfirm,
       "pktcEUERSTCHStatus": pktcEUERSTCHStatus,
       "pktcEUERSTCallXfrFeat": pktcEUERSTCallXfrFeat,
       "pktcEUERSTCallXfrTable": pktcEUERSTCallXfrTable,
       "pktcEUERSTCallXfrEntry": pktcEUERSTCallXfrEntry,
       "pktcEUERSTCXIndex": pktcEUERSTCXIndex,
       "pktcEUERSTCXNtfyTimeout": pktcEUERSTCXNtfyTimeout,
       "pktcEUERSTCXStatus": pktcEUERSTCXStatus,
       "pktcEUERSTCXInDialogRefer": pktcEUERSTCXInDialogRefer,
       "pktcEUERSTCXIncomingOnly": pktcEUERSTCXIncomingOnly,
       "pktcEUERSTDnDFeat": pktcEUERSTDnDFeat,
       "pktcEUERSTDnDTable": pktcEUERSTDnDTable,
       "pktcEUERSTDnDEntry": pktcEUERSTDnDEntry,
       "pktcEUERSTDnDIndex": pktcEUERSTDnDIndex,
       "pktcEUERSTDnDActConfirm": pktcEUERSTDnDActConfirm,
       "pktcEUERSTDnDDeActConfirm": pktcEUERSTDnDDeActConfirm,
       "pktcEUERSTDnDAUID": pktcEUERSTDnDAUID,
       "pktcEUERSTDnDStatus": pktcEUERSTDnDStatus,
       "pktcEUERSTMWIFeat": pktcEUERSTMWIFeat,
       "pktcEUERSTNfMWITable": pktcEUERSTNfMWITable,
       "pktcEUERSTNfMWIEntry": pktcEUERSTNfMWIEntry,
       "pktcEUERSTNfMWISubDuration": pktcEUERSTNfMWISubDuration,
       "pktcEUERSTNfMWIStatus": pktcEUERSTNfMWIStatus,
       "pktcEUERSTAutoRclFeat": pktcEUERSTAutoRclFeat,
       "pktcEUERSTAutoRclTable": pktcEUERSTAutoRclTable,
       "pktcEUERSTAutoRclEntry": pktcEUERSTAutoRclEntry,
       "pktcEUERSTARIndex": pktcEUERSTARIndex,
       "pktcEUERSTARTimer": pktcEUERSTARTimer,
       "pktcEUERSTARSpRngDuration": pktcEUERSTARSpRngDuration,
       "pktcEUERSTARSpRngRetryTime": pktcEUERSTARSpRngRetryTime,
       "pktcEUERSTARSpRngRetries": pktcEUERSTARSpRngRetries,
       "pktcEUERSTARMaxSubSend": pktcEUERSTARMaxSubSend,
       "pktcEUERSTARMaxSubRec": pktcEUERSTARMaxSubRec,
       "pktcEUERSTARStatus": pktcEUERSTARStatus,
       "pktcEUERSTAutoCbFeat": pktcEUERSTAutoCbFeat,
       "pktcEUERSTAutoCbTable": pktcEUERSTAutoCbTable,
       "pktcEUERSTAutoCbEntry": pktcEUERSTAutoCbEntry,
       "pktcEUERSTACbIndex": pktcEUERSTACbIndex,
       "pktcEUERSTACbTimer": pktcEUERSTACbTimer,
       "pktcEUERSTACbSpRngDuration": pktcEUERSTACbSpRngDuration,
       "pktcEUERSTACbSpRngRetryTime": pktcEUERSTACbSpRngRetryTime,
       "pktcEUERSTACbSpRngRetries": pktcEUERSTACbSpRngRetries,
       "pktcEUERSTACbMaxSubSend": pktcEUERSTACbMaxSubSend,
       "pktcEUERSTACbMaxSubRec": pktcEUERSTACbMaxSubRec,
       "pktcEUERSTACbStatus": pktcEUERSTACbStatus,
       "pktcEUERSTBusyLineVFeat": pktcEUERSTBusyLineVFeat,
       "pktcEUERSTNfBusyLineVTable": pktcEUERSTNfBusyLineVTable,
       "pktcEUERSTNfBusyLineVEntry": pktcEUERSTNfBusyLineVEntry,
       "pktcEUERSTNfBLVOperId": pktcEUERSTNfBLVOperId,
       "pktcEUERSTNfBLVStatus": pktcEUERSTNfBLVStatus,
       "pktcEUERSTEmSvcFeat": pktcEUERSTEmSvcFeat,
       "pktcEUERSTNfEmSvcTable": pktcEUERSTNfEmSvcTable,
       "pktcEUERSTNfEmSvcEntry": pktcEUERSTNfEmSvcEntry,
       "pktcEUERSTNfEmSvcNwHoldTimer": pktcEUERSTNfEmSvcNwHoldTimer,
       "pktcEUERSTNfEmSvcHowlTimer": pktcEUERSTNfEmSvcHowlTimer,
       "pktcEUERSTNfEmSvcDSCPValMedia": pktcEUERSTNfEmSvcDSCPValMedia,
       "pktcEUERSTNfEmSvcDSCPValSig": pktcEUERSTNfEmSvcDSCPValSig,
       "pktcEUERSTNfEmSvcStatus": pktcEUERSTNfEmSvcStatus,
       "pktcEUERSTSCFFeat": pktcEUERSTSCFFeat,
       "pktcEUERSTSCFTable": pktcEUERSTSCFTable,
       "pktcEUERSTSCFEntry": pktcEUERSTSCFEntry,
       "pktcEUERSTSCFIndex": pktcEUERSTSCFIndex,
       "pktcEUERSTSCFRingReminder": pktcEUERSTSCFRingReminder,
       "pktcEUERSTSCFAUID": pktcEUERSTSCFAUID,
       "pktcEUERSTSCFStatus": pktcEUERSTSCFStatus,
       "pktcEUERSTHeldMediaFeat": pktcEUERSTHeldMediaFeat,
       "pktcEUERSTHeldMediaTable": pktcEUERSTHeldMediaTable,
       "pktcEUERSTHeldMediaEntry": pktcEUERSTHeldMediaEntry,
       "pktcEUERSTHeldMediaIndex": pktcEUERSTHeldMediaIndex,
       "pktcEUERSTHeldMediaEnabled": pktcEUERSTHeldMediaEnabled,
       "pktcEUERSTHeldMediaStatus": pktcEUERSTHeldMediaStatus,
       "pktcEUERSTSpeedDialLocalMapFeat": pktcEUERSTSpeedDialLocalMapFeat,
       "pktcEUERSTSpeedDialLocalMapTable": pktcEUERSTSpeedDialLocalMapTable,
       "pktcEUERSTSpeedDialLocalMapEntry": pktcEUERSTSpeedDialLocalMapEntry,
       "pktcEUERSTSpeedDialLocalMapIndex": pktcEUERSTSpeedDialLocalMapIndex,
       "pktcEUERSTSpeedDialLocalMapId": pktcEUERSTSpeedDialLocalMapId,
       "pktcEUERSTSpeedDialLocalMapCode": pktcEUERSTSpeedDialLocalMapCode,
       "pktcEUERSTSpeedDialLocalMapDigitString": pktcEUERSTSpeedDialLocalMapDigitString,
       "pktcEUERSTSpeedDialLocalMapStatus": pktcEUERSTSpeedDialLocalMapStatus,
       "pktcEUERSTHotlineFeat": pktcEUERSTHotlineFeat,
       "pktcEUERSTHotlineTable": pktcEUERSTHotlineTable,
       "pktcEUERSTHotlineEntry": pktcEUERSTHotlineEntry,
       "pktcEUERSTHotlineIndex": pktcEUERSTHotlineIndex,
       "pktcEUERSTHotlineDestAddress": pktcEUERSTHotlineDestAddress,
       "pktcEUERSTHotlineOffhookTimer": pktcEUERSTHotlineOffhookTimer,
       "pktcEUERSTHotlineStatus": pktcEUERSTHotlineStatus,
       "pktcEUERST3WCallfeat": pktcEUERST3WCallfeat,
       "pktcEUERST3WCallTable": pktcEUERST3WCallTable,
       "pktcEUERST3WCallEntry": pktcEUERST3WCallEntry,
       "pktcEUERST3WCallIndex": pktcEUERST3WCallIndex,
       "pktcEUERST3WCallDisconnectTiming": pktcEUERST3WCallDisconnectTiming,
       "pktcEUERST3WCallStatus": pktcEUERST3WCallStatus,
       "pktcEUERSTConformance": pktcEUERSTConformance,
       "pktcEUERSTCompliances": pktcEUERSTCompliances,
       "pktcEUERSTCompliance": pktcEUERSTCompliance,
       "pktcEUERSTDeprecatedCompliance": pktcEUERSTDeprecatedCompliance,
       "pktcEUERSTGroups": pktcEUERSTGroups,
       "pktcEUERSTProfileGroup": pktcEUERSTProfileGroup,
       "pktcEUERSTBasicCallGroup": pktcEUERSTBasicCallGroup,
       "pktcEUERSTAncGroup": pktcEUERSTAncGroup,
       "pktcEUERSTUEStGroup": pktcEUERSTUEStGroup,
       "pktcEUERSTNoAnsGroup": pktcEUERSTNoAnsGroup,
       "pktcEUERSTCallerIDGroup": pktcEUERSTCallerIDGroup,
       "pktcEUERSTCallFwdGroup": pktcEUERSTCallFwdGroup,
       "pktcEUERSTCallHoldGroup": pktcEUERSTCallHoldGroup,
       "pktcEUERSTCallTransGroup": pktcEUERSTCallTransGroup,
       "pktcEUERSTDNDGroup": pktcEUERSTDNDGroup,
       "pktcEUERSTMWIGroup": pktcEUERSTMWIGroup,
       "pktcEUERSTAutoRecallGroup": pktcEUERSTAutoRecallGroup,
       "pktcEUERSTAutoCallbackGroup": pktcEUERSTAutoCallbackGroup,
       "pktcEUERSTBusyLineGroup": pktcEUERSTBusyLineGroup,
       "pktcEUERSTEmerSvcGroup": pktcEUERSTEmerSvcGroup,
       "pktcEUERSTDigitMapGroup": pktcEUERSTDigitMapGroup,
       "pktcEUERSTAppProfileGroup": pktcEUERSTAppProfileGroup,
       "pktcEUERSTSCFProfileGroup": pktcEUERSTSCFProfileGroup,
       "pktcEUERSTHeldMediaGroup": pktcEUERSTHeldMediaGroup,
       "pktcEUERSTSpeedDialLocalGroup": pktcEUERSTSpeedDialLocalGroup,
       "pktcEUERSTHotlineGroup": pktcEUERSTHotlineGroup,
       "pktcEUERSTCallWaitGroup": pktcEUERSTCallWaitGroup,
       "pktcEUERST3WCallGroup": pktcEUERST3WCallGroup,
       "pktcEUERSTDeprecated": pktcEUERSTDeprecated}
)
