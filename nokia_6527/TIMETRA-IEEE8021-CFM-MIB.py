# SNMP MIB module (TIMETRA-IEEE8021-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-IEEE8021-CFM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:44:24 2025
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

(Dot1agCfmIdPermission,
 Dot1agCfmLowestAlarmPri,
 Dot1agCfmMDLevel,
 Dot1agCfmMepId,
 Dot1agCfmMepIdOrZero,
 Dot1agCfmMpDirection,
 VlanIdOrNone,
 dot1agCfmMaCompEntry,
 dot1agCfmMaIndex,
 dot1agCfmMaMepListEntry,
 dot1agCfmMaNetEntry,
 dot1agCfmMdEntry,
 dot1agCfmMdIndex,
 dot1agCfmMepDbEntry,
 dot1agCfmMepEntry,
 dot1agCfmMepIdentifier,
 dot1agCfmMepTransmitLbmDestMacAddress,
 dot1agCfmMepTransmitLtmSeqNumber) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmIdPermission",
    "Dot1agCfmLowestAlarmPri",
    "Dot1agCfmMDLevel",
    "Dot1agCfmMepId",
    "Dot1agCfmMepIdOrZero",
    "Dot1agCfmMpDirection",
    "VlanIdOrNone",
    "dot1agCfmMaCompEntry",
    "dot1agCfmMaIndex",
    "dot1agCfmMaMepListEntry",
    "dot1agCfmMaNetEntry",
    "dot1agCfmMdEntry",
    "dot1agCfmMdIndex",
    "dot1agCfmMepDbEntry",
    "dot1agCfmMepEntry",
    "dot1agCfmMepIdentifier",
    "dot1agCfmMepTransmitLbmDestMacAddress",
    "dot1agCfmMepTransmitLtmSeqNumber")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(LldpChassisIdSubtype,) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisIdSubtype")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrNone")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(SdpId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "SdpId")

(TItemDescription,
 TNamedItem,
 TmnxCreateOrigin,
 TmnxEnabledDisabled,
 TmnxServId) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TmnxCreateOrigin",
    "TmnxEnabledDisabled",
    "TmnxServId")


# MODULE-IDENTITY

timetraIEEE8021CfmMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 52)
)
if mibBuilder.loadTexts:
    timetraIEEE8021CfmMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Dot1agCfmStatisticOpcodeName(TextualConvention, Integer32):
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ccm", 2),
          ("lbr", 3),
          ("lbm", 4),
          ("ltr", 5),
          ("ltm", 6),
          ("ais", 7),
          ("lck", 8),
          ("tst", 9),
          ("laps", 10),
          ("raps", 11),
          ("mcc", 12),
          ("lmr", 13),
          ("lmm", 14),
          ("odm", 15),
          ("dmr", 16),
          ("dmm", 17),
          ("exr", 18),
          ("exm", 19),
          ("csf", 20),
          ("vsr", 21),
          ("vsm", 22),
          ("osl", 23),
          ("slr", 24),
          ("slm", 25))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxDot1agMIBConformance_ObjectIdentity = ObjectIdentity
tmnxDot1agMIBConformance = _TmnxDot1agMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52)
)
_TmnxDot1agCfmCompliances_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmCompliances = _TmnxDot1agCfmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 1)
)
_TmnxDot1agCfmGroups_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmGroups = _TmnxDot1agCfmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2)
)
_TmnxDot1agCfmV6v0Groups_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmV6v0Groups = _TmnxDot1agCfmV6v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 10)
)
_TmnxDot1agCfmV7v0Groups_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmV7v0Groups = _TmnxDot1agCfmV7v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 11)
)
_TmnxDot1agCfmV8v0Groups_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmV8v0Groups = _TmnxDot1agCfmV8v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 12)
)
_TmnxDot1agCfmV9v0Groups_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmV9v0Groups = _TmnxDot1agCfmV9v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 13)
)
_TmnxDot1agCfmV10v0Groups_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmV10v0Groups = _TmnxDot1agCfmV10v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 14)
)
_TmnxDot1agCfmV11v0Groups_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmV11v0Groups = _TmnxDot1agCfmV11v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 15)
)
_TmnxDot1agCfmV12v0Groups_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmV12v0Groups = _TmnxDot1agCfmV12v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 16)
)
_TmnxDot1agMIBObjs_ObjectIdentity = ObjectIdentity
tmnxDot1agMIBObjs = _TmnxDot1agMIBObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52)
)
_TmnxDot1agCfmStack_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmStack = _TmnxDot1agCfmStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1)
)
_TmnxDot1agCfmSdpBindStackTable_Object = MibTable
tmnxDot1agCfmSdpBindStackTable = _TmnxDot1agCfmSdpBindStackTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpBindStackTable.setStatus("current")
_TmnxDot1agCfmSdpBindStackEntry_Object = MibTableRow
tmnxDot1agCfmSdpBindStackEntry = _TmnxDot1agCfmSdpBindStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 1, 1)
)
tmnxDot1agCfmSdpBindStackEntry.setIndexNames(
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpBindStackSdpId"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpBindStackVcId"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpBindStackMdLevel"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpBindStackDirection"),
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpBindStackEntry.setStatus("current")
_TmnxDot1agCfmSdpBindStackSdpId_Type = SdpId
_TmnxDot1agCfmSdpBindStackSdpId_Object = MibTableColumn
tmnxDot1agCfmSdpBindStackSdpId = _TmnxDot1agCfmSdpBindStackSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 1, 1, 1),
    _TmnxDot1agCfmSdpBindStackSdpId_Type()
)
tmnxDot1agCfmSdpBindStackSdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpBindStackSdpId.setStatus("current")
_TmnxDot1agCfmSdpBindStackVcId_Type = Unsigned32
_TmnxDot1agCfmSdpBindStackVcId_Object = MibTableColumn
tmnxDot1agCfmSdpBindStackVcId = _TmnxDot1agCfmSdpBindStackVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 1, 1, 2),
    _TmnxDot1agCfmSdpBindStackVcId_Type()
)
tmnxDot1agCfmSdpBindStackVcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpBindStackVcId.setStatus("current")
_TmnxDot1agCfmSdpBindStackMdLevel_Type = Dot1agCfmMDLevel
_TmnxDot1agCfmSdpBindStackMdLevel_Object = MibTableColumn
tmnxDot1agCfmSdpBindStackMdLevel = _TmnxDot1agCfmSdpBindStackMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 1, 1, 3),
    _TmnxDot1agCfmSdpBindStackMdLevel_Type()
)
tmnxDot1agCfmSdpBindStackMdLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpBindStackMdLevel.setStatus("current")
_TmnxDot1agCfmSdpBindStackDirection_Type = Dot1agCfmMpDirection
_TmnxDot1agCfmSdpBindStackDirection_Object = MibTableColumn
tmnxDot1agCfmSdpBindStackDirection = _TmnxDot1agCfmSdpBindStackDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 1, 1, 4),
    _TmnxDot1agCfmSdpBindStackDirection_Type()
)
tmnxDot1agCfmSdpBindStackDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpBindStackDirection.setStatus("current")
_TmnxDot1agCfmSdpBindStackMdIndex_Type = Unsigned32
_TmnxDot1agCfmSdpBindStackMdIndex_Object = MibTableColumn
tmnxDot1agCfmSdpBindStackMdIndex = _TmnxDot1agCfmSdpBindStackMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 1, 1, 5),
    _TmnxDot1agCfmSdpBindStackMdIndex_Type()
)
tmnxDot1agCfmSdpBindStackMdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpBindStackMdIndex.setStatus("current")
_TmnxDot1agCfmSdpBindStackMaIndex_Type = Unsigned32
_TmnxDot1agCfmSdpBindStackMaIndex_Object = MibTableColumn
tmnxDot1agCfmSdpBindStackMaIndex = _TmnxDot1agCfmSdpBindStackMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 1, 1, 6),
    _TmnxDot1agCfmSdpBindStackMaIndex_Type()
)
tmnxDot1agCfmSdpBindStackMaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpBindStackMaIndex.setStatus("current")
_TmnxDot1agCfmSdpBindStackMepId_Type = Dot1agCfmMepIdOrZero
_TmnxDot1agCfmSdpBindStackMepId_Object = MibTableColumn
tmnxDot1agCfmSdpBindStackMepId = _TmnxDot1agCfmSdpBindStackMepId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 1, 1, 7),
    _TmnxDot1agCfmSdpBindStackMepId_Type()
)
tmnxDot1agCfmSdpBindStackMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpBindStackMepId.setStatus("current")
_TmnxDot1agCfmSdpBindStackMacAddress_Type = MacAddress
_TmnxDot1agCfmSdpBindStackMacAddress_Object = MibTableColumn
tmnxDot1agCfmSdpBindStackMacAddress = _TmnxDot1agCfmSdpBindStackMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 1, 1, 8),
    _TmnxDot1agCfmSdpBindStackMacAddress_Type()
)
tmnxDot1agCfmSdpBindStackMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpBindStackMacAddress.setStatus("current")
_TmnxDot1agCfmStackTable_Object = MibTable
tmnxDot1agCfmStackTable = _TmnxDot1agCfmStackTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmStackTable.setStatus("current")
_TmnxDot1agCfmStackEntry_Object = MibTableRow
tmnxDot1agCfmStackEntry = _TmnxDot1agCfmStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 2, 1)
)
tmnxDot1agCfmStackEntry.setIndexNames(
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmStackifIndex"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmStackVlanIdOrNone"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmStackMdLevel"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmStackDirection"),
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmStackEntry.setStatus("current")
_TmnxDot1agCfmStackifIndex_Type = InterfaceIndex
_TmnxDot1agCfmStackifIndex_Object = MibTableColumn
tmnxDot1agCfmStackifIndex = _TmnxDot1agCfmStackifIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 2, 1, 1),
    _TmnxDot1agCfmStackifIndex_Type()
)
tmnxDot1agCfmStackifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmStackifIndex.setStatus("current")
_TmnxDot1agCfmStackVlanIdOrNone_Type = Unsigned32
_TmnxDot1agCfmStackVlanIdOrNone_Object = MibTableColumn
tmnxDot1agCfmStackVlanIdOrNone = _TmnxDot1agCfmStackVlanIdOrNone_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 2, 1, 2),
    _TmnxDot1agCfmStackVlanIdOrNone_Type()
)
tmnxDot1agCfmStackVlanIdOrNone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmStackVlanIdOrNone.setStatus("current")
_TmnxDot1agCfmStackMdLevel_Type = Dot1agCfmMDLevel
_TmnxDot1agCfmStackMdLevel_Object = MibTableColumn
tmnxDot1agCfmStackMdLevel = _TmnxDot1agCfmStackMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 2, 1, 3),
    _TmnxDot1agCfmStackMdLevel_Type()
)
tmnxDot1agCfmStackMdLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmStackMdLevel.setStatus("current")
_TmnxDot1agCfmStackDirection_Type = Dot1agCfmMpDirection
_TmnxDot1agCfmStackDirection_Object = MibTableColumn
tmnxDot1agCfmStackDirection = _TmnxDot1agCfmStackDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 2, 1, 4),
    _TmnxDot1agCfmStackDirection_Type()
)
tmnxDot1agCfmStackDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmStackDirection.setStatus("current")
_TmnxDot1agCfmStackMdIndex_Type = Unsigned32
_TmnxDot1agCfmStackMdIndex_Object = MibTableColumn
tmnxDot1agCfmStackMdIndex = _TmnxDot1agCfmStackMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 2, 1, 5),
    _TmnxDot1agCfmStackMdIndex_Type()
)
tmnxDot1agCfmStackMdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmStackMdIndex.setStatus("current")
_TmnxDot1agCfmStackMaIndex_Type = Unsigned32
_TmnxDot1agCfmStackMaIndex_Object = MibTableColumn
tmnxDot1agCfmStackMaIndex = _TmnxDot1agCfmStackMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 2, 1, 6),
    _TmnxDot1agCfmStackMaIndex_Type()
)
tmnxDot1agCfmStackMaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmStackMaIndex.setStatus("current")
_TmnxDot1agCfmStackMepId_Type = Dot1agCfmMepIdOrZero
_TmnxDot1agCfmStackMepId_Object = MibTableColumn
tmnxDot1agCfmStackMepId = _TmnxDot1agCfmStackMepId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 2, 1, 7),
    _TmnxDot1agCfmStackMepId_Type()
)
tmnxDot1agCfmStackMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmStackMepId.setStatus("current")
_TmnxDot1agCfmStackMacAddress_Type = MacAddress
_TmnxDot1agCfmStackMacAddress_Object = MibTableColumn
tmnxDot1agCfmStackMacAddress = _TmnxDot1agCfmStackMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 2, 1, 8),
    _TmnxDot1agCfmStackMacAddress_Type()
)
tmnxDot1agCfmStackMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmStackMacAddress.setStatus("current")


class _TmnxDot1agCfmStackMPType_Type(Integer32):
    """Custom type tmnxDot1agCfmStackMPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("sap", 1),
          ("ethTun", 2),
          ("ethRing", 3),
          ("facPort", 4),
          ("facInterface", 5))
    )


_TmnxDot1agCfmStackMPType_Type.__name__ = "Integer32"
_TmnxDot1agCfmStackMPType_Object = MibTableColumn
tmnxDot1agCfmStackMPType = _TmnxDot1agCfmStackMPType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 2, 1, 9),
    _TmnxDot1agCfmStackMPType_Type()
)
tmnxDot1agCfmStackMPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmStackMPType.setStatus("current")
_TmnxDot1agCfmVStackTable_Object = MibTable
tmnxDot1agCfmVStackTable = _TmnxDot1agCfmVStackTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmVStackTable.setStatus("current")
_TmnxDot1agCfmVStackEntry_Object = MibTableRow
tmnxDot1agCfmVStackEntry = _TmnxDot1agCfmVStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 3, 1)
)
tmnxDot1agCfmVStackEntry.setIndexNames(
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmVStackSvcId"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmVStackMdLevel"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmVStackDirection"),
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmVStackEntry.setStatus("current")
_TmnxDot1agCfmVStackSvcId_Type = TmnxServId
_TmnxDot1agCfmVStackSvcId_Object = MibTableColumn
tmnxDot1agCfmVStackSvcId = _TmnxDot1agCfmVStackSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 3, 1, 1),
    _TmnxDot1agCfmVStackSvcId_Type()
)
tmnxDot1agCfmVStackSvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmVStackSvcId.setStatus("current")
_TmnxDot1agCfmVStackMdLevel_Type = Dot1agCfmMDLevel
_TmnxDot1agCfmVStackMdLevel_Object = MibTableColumn
tmnxDot1agCfmVStackMdLevel = _TmnxDot1agCfmVStackMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 3, 1, 2),
    _TmnxDot1agCfmVStackMdLevel_Type()
)
tmnxDot1agCfmVStackMdLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmVStackMdLevel.setStatus("current")
_TmnxDot1agCfmVStackDirection_Type = Dot1agCfmMpDirection
_TmnxDot1agCfmVStackDirection_Object = MibTableColumn
tmnxDot1agCfmVStackDirection = _TmnxDot1agCfmVStackDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 3, 1, 3),
    _TmnxDot1agCfmVStackDirection_Type()
)
tmnxDot1agCfmVStackDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmVStackDirection.setStatus("current")
_TmnxDot1agCfmVStackMdIndex_Type = Unsigned32
_TmnxDot1agCfmVStackMdIndex_Object = MibTableColumn
tmnxDot1agCfmVStackMdIndex = _TmnxDot1agCfmVStackMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 3, 1, 4),
    _TmnxDot1agCfmVStackMdIndex_Type()
)
tmnxDot1agCfmVStackMdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmVStackMdIndex.setStatus("current")
_TmnxDot1agCfmVStackMaIndex_Type = Unsigned32
_TmnxDot1agCfmVStackMaIndex_Object = MibTableColumn
tmnxDot1agCfmVStackMaIndex = _TmnxDot1agCfmVStackMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 3, 1, 5),
    _TmnxDot1agCfmVStackMaIndex_Type()
)
tmnxDot1agCfmVStackMaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmVStackMaIndex.setStatus("current")
_TmnxDot1agCfmVStackMepId_Type = Dot1agCfmMepIdOrZero
_TmnxDot1agCfmVStackMepId_Object = MibTableColumn
tmnxDot1agCfmVStackMepId = _TmnxDot1agCfmVStackMepId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 3, 1, 6),
    _TmnxDot1agCfmVStackMepId_Type()
)
tmnxDot1agCfmVStackMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmVStackMepId.setStatus("current")
_TmnxDot1agCfmVStackMacAddress_Type = MacAddress
_TmnxDot1agCfmVStackMacAddress_Object = MibTableColumn
tmnxDot1agCfmVStackMacAddress = _TmnxDot1agCfmVStackMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 3, 1, 7),
    _TmnxDot1agCfmVStackMacAddress_Type()
)
tmnxDot1agCfmVStackMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmVStackMacAddress.setStatus("current")
_TmnxDot1agCfmPVStackTable_Object = MibTable
tmnxDot1agCfmPVStackTable = _TmnxDot1agCfmPVStackTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmPVStackTable.setStatus("current")
_TmnxDot1agCfmPVStackEntry_Object = MibTableRow
tmnxDot1agCfmPVStackEntry = _TmnxDot1agCfmPVStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 4, 1)
)
tmnxDot1agCfmPVStackEntry.setIndexNames(
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmPVStackifIndex"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmPVStackVlanIdOrNone"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmPVStackPriVlanId"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmPVStackMdLevel"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmPVStackDirection"),
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmPVStackEntry.setStatus("current")
_TmnxDot1agCfmPVStackifIndex_Type = InterfaceIndex
_TmnxDot1agCfmPVStackifIndex_Object = MibTableColumn
tmnxDot1agCfmPVStackifIndex = _TmnxDot1agCfmPVStackifIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 4, 1, 1),
    _TmnxDot1agCfmPVStackifIndex_Type()
)
tmnxDot1agCfmPVStackifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmPVStackifIndex.setStatus("current")
_TmnxDot1agCfmPVStackVlanIdOrNone_Type = Unsigned32
_TmnxDot1agCfmPVStackVlanIdOrNone_Object = MibTableColumn
tmnxDot1agCfmPVStackVlanIdOrNone = _TmnxDot1agCfmPVStackVlanIdOrNone_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 4, 1, 2),
    _TmnxDot1agCfmPVStackVlanIdOrNone_Type()
)
tmnxDot1agCfmPVStackVlanIdOrNone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmPVStackVlanIdOrNone.setStatus("current")
_TmnxDot1agCfmPVStackPriVlanId_Type = Unsigned32
_TmnxDot1agCfmPVStackPriVlanId_Object = MibTableColumn
tmnxDot1agCfmPVStackPriVlanId = _TmnxDot1agCfmPVStackPriVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 4, 1, 3),
    _TmnxDot1agCfmPVStackPriVlanId_Type()
)
tmnxDot1agCfmPVStackPriVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmPVStackPriVlanId.setStatus("current")
_TmnxDot1agCfmPVStackMdLevel_Type = Dot1agCfmMDLevel
_TmnxDot1agCfmPVStackMdLevel_Object = MibTableColumn
tmnxDot1agCfmPVStackMdLevel = _TmnxDot1agCfmPVStackMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 4, 1, 4),
    _TmnxDot1agCfmPVStackMdLevel_Type()
)
tmnxDot1agCfmPVStackMdLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmPVStackMdLevel.setStatus("current")
_TmnxDot1agCfmPVStackDirection_Type = Dot1agCfmMpDirection
_TmnxDot1agCfmPVStackDirection_Object = MibTableColumn
tmnxDot1agCfmPVStackDirection = _TmnxDot1agCfmPVStackDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 4, 1, 5),
    _TmnxDot1agCfmPVStackDirection_Type()
)
tmnxDot1agCfmPVStackDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmPVStackDirection.setStatus("current")
_TmnxDot1agCfmPVStackMdIndex_Type = Unsigned32
_TmnxDot1agCfmPVStackMdIndex_Object = MibTableColumn
tmnxDot1agCfmPVStackMdIndex = _TmnxDot1agCfmPVStackMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 4, 1, 6),
    _TmnxDot1agCfmPVStackMdIndex_Type()
)
tmnxDot1agCfmPVStackMdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmPVStackMdIndex.setStatus("current")
_TmnxDot1agCfmPVStackMaIndex_Type = Unsigned32
_TmnxDot1agCfmPVStackMaIndex_Object = MibTableColumn
tmnxDot1agCfmPVStackMaIndex = _TmnxDot1agCfmPVStackMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 4, 1, 7),
    _TmnxDot1agCfmPVStackMaIndex_Type()
)
tmnxDot1agCfmPVStackMaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmPVStackMaIndex.setStatus("current")
_TmnxDot1agCfmPVStackMepId_Type = Dot1agCfmMepIdOrZero
_TmnxDot1agCfmPVStackMepId_Object = MibTableColumn
tmnxDot1agCfmPVStackMepId = _TmnxDot1agCfmPVStackMepId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 4, 1, 8),
    _TmnxDot1agCfmPVStackMepId_Type()
)
tmnxDot1agCfmPVStackMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmPVStackMepId.setStatus("current")
_TmnxDot1agCfmPVStackMacAddress_Type = MacAddress
_TmnxDot1agCfmPVStackMacAddress_Object = MibTableColumn
tmnxDot1agCfmPVStackMacAddress = _TmnxDot1agCfmPVStackMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 1, 4, 1, 9),
    _TmnxDot1agCfmPVStackMacAddress_Type()
)
tmnxDot1agCfmPVStackMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmPVStackMacAddress.setStatus("current")
_TmnxDot1agCfmGlobalObjs_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmGlobalObjs = _TmnxDot1agCfmGlobalObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2)
)
_TmnxDot1agCfmMcLagConfigGroup_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmMcLagConfigGroup = _TmnxDot1agCfmMcLagConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 1)
)


class _TmnxDot1agCfmMcLagStdbyInactive_Type(TruthValue):
    """Custom type tmnxDot1agCfmMcLagStdbyInactive based on TruthValue"""
    defaultValue = 2


_TmnxDot1agCfmMcLagStdbyInactive_Type.__name__ = "TruthValue"
_TmnxDot1agCfmMcLagStdbyInactive_Object = MibScalar
tmnxDot1agCfmMcLagStdbyInactive = _TmnxDot1agCfmMcLagStdbyInactive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 1, 1),
    _TmnxDot1agCfmMcLagStdbyInactive_Type()
)
tmnxDot1agCfmMcLagStdbyInactive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMcLagStdbyInactive.setStatus("current")


class _TmnxDot1agCfmMcLagPropHoldTime_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMcLagPropHoldTime based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_TmnxDot1agCfmMcLagPropHoldTime_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMcLagPropHoldTime_Object = MibScalar
tmnxDot1agCfmMcLagPropHoldTime = _TmnxDot1agCfmMcLagPropHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 1, 2),
    _TmnxDot1agCfmMcLagPropHoldTime_Type()
)
tmnxDot1agCfmMcLagPropHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMcLagPropHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMcLagPropHoldTime.setUnits("seconds")
_TmnxDot1agCfmSLMConfigGroup_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmSLMConfigGroup = _TmnxDot1agCfmSLMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 2)
)


class _TmnxDot1agCfmSLMInactivityTimer_Type(Unsigned32):
    """Custom type tmnxDot1agCfmSLMInactivityTimer based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_TmnxDot1agCfmSLMInactivityTimer_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmSLMInactivityTimer_Object = MibScalar
tmnxDot1agCfmSLMInactivityTimer = _TmnxDot1agCfmSLMInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 2, 1),
    _TmnxDot1agCfmSLMInactivityTimer_Type()
)
tmnxDot1agCfmSLMInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSLMInactivityTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSLMInactivityTimer.setUnits("seconds")
_TmnxDot1agCfmStatisticsGroup_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmStatisticsGroup = _TmnxDot1agCfmStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3)
)
_TmnxDot1agCfmGlobalPacketStats_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmGlobalPacketStats = _TmnxDot1agCfmGlobalPacketStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 1)
)
_TmnxDot1agCfmGlobalPacketRxCount_Type = Counter32
_TmnxDot1agCfmGlobalPacketRxCount_Object = MibScalar
tmnxDot1agCfmGlobalPacketRxCount = _TmnxDot1agCfmGlobalPacketRxCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 1, 1),
    _TmnxDot1agCfmGlobalPacketRxCount_Type()
)
tmnxDot1agCfmGlobalPacketRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalPacketRxCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalPacketRxCount.setUnits("packets")
_TmnxDot1agCfmGlobalPacketTxCount_Type = Counter32
_TmnxDot1agCfmGlobalPacketTxCount_Object = MibScalar
tmnxDot1agCfmGlobalPacketTxCount = _TmnxDot1agCfmGlobalPacketTxCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 1, 2),
    _TmnxDot1agCfmGlobalPacketTxCount_Type()
)
tmnxDot1agCfmGlobalPacketTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalPacketTxCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalPacketTxCount.setUnits("packets")
_TmnxDot1agCfmGlobalPacketDropped_Type = Counter32
_TmnxDot1agCfmGlobalPacketDropped_Object = MibScalar
tmnxDot1agCfmGlobalPacketDropped = _TmnxDot1agCfmGlobalPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 1, 3),
    _TmnxDot1agCfmGlobalPacketDropped_Type()
)
tmnxDot1agCfmGlobalPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalPacketDropped.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalPacketDropped.setUnits("packets")
_TmnxDot1agCfmGlobalPacketDiscard_Type = Counter32
_TmnxDot1agCfmGlobalPacketDiscard_Object = MibScalar
tmnxDot1agCfmGlobalPacketDiscard = _TmnxDot1agCfmGlobalPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 1, 4),
    _TmnxDot1agCfmGlobalPacketDiscard_Type()
)
tmnxDot1agCfmGlobalPacketDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalPacketDiscard.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalPacketDiscard.setUnits("packets")
_TmnxDot1agCfmGlobalAisTxActive_Type = Counter32
_TmnxDot1agCfmGlobalAisTxActive_Object = MibScalar
tmnxDot1agCfmGlobalAisTxActive = _TmnxDot1agCfmGlobalAisTxActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 1, 5),
    _TmnxDot1agCfmGlobalAisTxActive_Type()
)
tmnxDot1agCfmGlobalAisTxActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalAisTxActive.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalAisTxActive.setUnits("sessions")
_TmnxDot1agCfmGlobalAisTxFail_Type = Counter32
_TmnxDot1agCfmGlobalAisTxFail_Object = MibScalar
tmnxDot1agCfmGlobalAisTxFail = _TmnxDot1agCfmGlobalAisTxFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 1, 6),
    _TmnxDot1agCfmGlobalAisTxFail_Type()
)
tmnxDot1agCfmGlobalAisTxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalAisTxFail.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalAisTxFail.setUnits("sessions")
_TmnxDot1agCfmComponentLimitTable_Object = MibTable
tmnxDot1agCfmComponentLimitTable = _TmnxDot1agCfmComponentLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmComponentLimitTable.setStatus("current")
_TmnxDot1agCfmComponentLimitEntry_Object = MibTableRow
tmnxDot1agCfmComponentLimitEntry = _TmnxDot1agCfmComponentLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 2, 1)
)
tmnxDot1agCfmComponentLimitEntry.setIndexNames(
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmCompMajorIndex"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmCompMinorIndex"),
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmComponentLimitEntry.setStatus("current")
_TmnxDot1agCfmCompMajorIndex_Type = Unsigned32
_TmnxDot1agCfmCompMajorIndex_Object = MibTableColumn
tmnxDot1agCfmCompMajorIndex = _TmnxDot1agCfmCompMajorIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 2, 1, 1),
    _TmnxDot1agCfmCompMajorIndex_Type()
)
tmnxDot1agCfmCompMajorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmCompMajorIndex.setStatus("current")
_TmnxDot1agCfmCompMinorIndex_Type = Unsigned32
_TmnxDot1agCfmCompMinorIndex_Object = MibTableColumn
tmnxDot1agCfmCompMinorIndex = _TmnxDot1agCfmCompMinorIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 2, 1, 2),
    _TmnxDot1agCfmCompMinorIndex_Type()
)
tmnxDot1agCfmCompMinorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmCompMinorIndex.setStatus("current")
_TmnxDot1agCfmCompName_Type = TNamedItem
_TmnxDot1agCfmCompName_Object = MibTableColumn
tmnxDot1agCfmCompName = _TmnxDot1agCfmCompName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 2, 1, 3),
    _TmnxDot1agCfmCompName_Type()
)
tmnxDot1agCfmCompName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmCompName.setStatus("current")
_TmnxDot1agCfmCompResourceUsage_Type = Unsigned32
_TmnxDot1agCfmCompResourceUsage_Object = MibTableColumn
tmnxDot1agCfmCompResourceUsage = _TmnxDot1agCfmCompResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 2, 1, 4),
    _TmnxDot1agCfmCompResourceUsage_Type()
)
tmnxDot1agCfmCompResourceUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmCompResourceUsage.setStatus("current")
_TmnxDot1agCfmCompResourceLimit_Type = Unsigned32
_TmnxDot1agCfmCompResourceLimit_Object = MibTableColumn
tmnxDot1agCfmCompResourceLimit = _TmnxDot1agCfmCompResourceLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 2, 1, 5),
    _TmnxDot1agCfmCompResourceLimit_Type()
)
tmnxDot1agCfmCompResourceLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmCompResourceLimit.setStatus("current")
_TmnxDot1agCfmGlobalOpcodeTable_Object = MibTable
tmnxDot1agCfmGlobalOpcodeTable = _TmnxDot1agCfmGlobalOpcodeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalOpcodeTable.setStatus("current")
_TmnxDot1agCfmGlobalOpcodeEntry_Object = MibTableRow
tmnxDot1agCfmGlobalOpcodeEntry = _TmnxDot1agCfmGlobalOpcodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 3, 1)
)
tmnxDot1agCfmGlobalOpcodeEntry.setIndexNames(
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGlobalOpcode"),
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalOpcodeEntry.setStatus("current")
_TmnxDot1agCfmGlobalOpcode_Type = Dot1agCfmStatisticOpcodeName
_TmnxDot1agCfmGlobalOpcode_Object = MibTableColumn
tmnxDot1agCfmGlobalOpcode = _TmnxDot1agCfmGlobalOpcode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 3, 1, 1),
    _TmnxDot1agCfmGlobalOpcode_Type()
)
tmnxDot1agCfmGlobalOpcode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalOpcode.setStatus("current")
_TmnxDot1agCfmGlobalOpcodeRx_Type = Counter32
_TmnxDot1agCfmGlobalOpcodeRx_Object = MibTableColumn
tmnxDot1agCfmGlobalOpcodeRx = _TmnxDot1agCfmGlobalOpcodeRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 3, 1, 2),
    _TmnxDot1agCfmGlobalOpcodeRx_Type()
)
tmnxDot1agCfmGlobalOpcodeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalOpcodeRx.setStatus("current")
_TmnxDot1agCfmGlobalOpcodeTx_Type = Counter32
_TmnxDot1agCfmGlobalOpcodeTx_Object = MibTableColumn
tmnxDot1agCfmGlobalOpcodeTx = _TmnxDot1agCfmGlobalOpcodeTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 3, 3, 1, 3),
    _TmnxDot1agCfmGlobalOpcodeTx_Type()
)
tmnxDot1agCfmGlobalOpcodeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalOpcodeTx.setStatus("current")
_TmnxDot1agCfmSystemScalarsGroup_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmSystemScalarsGroup = _TmnxDot1agCfmSystemScalarsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 4)
)


class _TmnxDot1agCfmGraceTxEnable_Type(TruthValue):
    """Custom type tmnxDot1agCfmGraceTxEnable based on TruthValue"""
    defaultValue = 1


_TmnxDot1agCfmGraceTxEnable_Type.__name__ = "TruthValue"
_TmnxDot1agCfmGraceTxEnable_Object = MibScalar
tmnxDot1agCfmGraceTxEnable = _TmnxDot1agCfmGraceTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 4, 1),
    _TmnxDot1agCfmGraceTxEnable_Type()
)
tmnxDot1agCfmGraceTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot1agCfmGraceTxEnable.setStatus("current")
_TmnxDot1agCfmGracePeriod_Type = TruthValue
_TmnxDot1agCfmGracePeriod_Object = MibScalar
tmnxDot1agCfmGracePeriod = _TmnxDot1agCfmGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 4, 2),
    _TmnxDot1agCfmGracePeriod_Type()
)
tmnxDot1agCfmGracePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmGracePeriod.setStatus("current")


class _TmnxDot1agCfmSenderIdType_Type(LldpChassisIdSubtype):
    """Custom type tmnxDot1agCfmSenderIdType based on LldpChassisIdSubtype"""
    defaultValue = 1


_TmnxDot1agCfmSenderIdType_Type.__name__ = "LldpChassisIdSubtype"
_TmnxDot1agCfmSenderIdType_Object = MibScalar
tmnxDot1agCfmSenderIdType = _TmnxDot1agCfmSenderIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 4, 3),
    _TmnxDot1agCfmSenderIdType_Type()
)
tmnxDot1agCfmSenderIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSenderIdType.setStatus("current")


class _TmnxDot1agCfmSenderIdName_Type(OctetString):
    """Custom type tmnxDot1agCfmSenderIdName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_TmnxDot1agCfmSenderIdName_Type.__name__ = "OctetString"
_TmnxDot1agCfmSenderIdName_Object = MibScalar
tmnxDot1agCfmSenderIdName = _TmnxDot1agCfmSenderIdName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 2, 4, 4),
    _TmnxDot1agCfmSenderIdName_Type()
)
tmnxDot1agCfmSenderIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSenderIdName.setStatus("current")
_TmnxDot1agCfmManagementObjects_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmManagementObjects = _TmnxDot1agCfmManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 3)
)
_TmnxDot1agCfmMepMgmtTable_Object = MibTable
tmnxDot1agCfmMepMgmtTable = _TmnxDot1agCfmMepMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepMgmtTable.setStatus("current")
_TmnxDot1agCfmMepMgmtEntry_Object = MibTableRow
tmnxDot1agCfmMepMgmtEntry = _TmnxDot1agCfmMepMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepMgmtEntry.setStatus("current")
_TmnxDot1agCfmMepMgmtRowStatus_Type = RowStatus
_TmnxDot1agCfmMepMgmtRowStatus_Object = MibTableColumn
tmnxDot1agCfmMepMgmtRowStatus = _TmnxDot1agCfmMepMgmtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 3, 1, 1, 1),
    _TmnxDot1agCfmMepMgmtRowStatus_Type()
)
tmnxDot1agCfmMepMgmtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepMgmtRowStatus.setStatus("current")


class _TmnxDot1agCfmMepMgmtType_Type(Integer32):
    """Custom type tmnxDot1agCfmMepMgmtType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("facilityPort", 1),
          ("facilityInterface", 2),
          ("sapPrimaryVlan", 3))
    )


_TmnxDot1agCfmMepMgmtType_Type.__name__ = "Integer32"
_TmnxDot1agCfmMepMgmtType_Object = MibTableColumn
tmnxDot1agCfmMepMgmtType = _TmnxDot1agCfmMepMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 3, 1, 1, 2),
    _TmnxDot1agCfmMepMgmtType_Type()
)
tmnxDot1agCfmMepMgmtType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepMgmtType.setStatus("current")
_TmnxDot1agCfmMepMgmtServiceId_Type = TmnxServId
_TmnxDot1agCfmMepMgmtServiceId_Object = MibTableColumn
tmnxDot1agCfmMepMgmtServiceId = _TmnxDot1agCfmMepMgmtServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 3, 1, 1, 3),
    _TmnxDot1agCfmMepMgmtServiceId_Type()
)
tmnxDot1agCfmMepMgmtServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepMgmtServiceId.setStatus("current")
_TmnxDot1agCfmMepMgmtIfIndex_Type = InterfaceIndexOrZero
_TmnxDot1agCfmMepMgmtIfIndex_Object = MibTableColumn
tmnxDot1agCfmMepMgmtIfIndex = _TmnxDot1agCfmMepMgmtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 3, 1, 1, 4),
    _TmnxDot1agCfmMepMgmtIfIndex_Type()
)
tmnxDot1agCfmMepMgmtIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepMgmtIfIndex.setStatus("current")
_TmnxDot1agCfmMepMgmtPrimaryVid_Type = Unsigned32
_TmnxDot1agCfmMepMgmtPrimaryVid_Object = MibTableColumn
tmnxDot1agCfmMepMgmtPrimaryVid = _TmnxDot1agCfmMepMgmtPrimaryVid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 3, 1, 1, 5),
    _TmnxDot1agCfmMepMgmtPrimaryVid_Type()
)
tmnxDot1agCfmMepMgmtPrimaryVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepMgmtPrimaryVid.setStatus("current")
_TmnxDot1agCfmMepMgmtSdpId_Type = SdpId
_TmnxDot1agCfmMepMgmtSdpId_Object = MibTableColumn
tmnxDot1agCfmMepMgmtSdpId = _TmnxDot1agCfmMepMgmtSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 3, 1, 1, 6),
    _TmnxDot1agCfmMepMgmtSdpId_Type()
)
tmnxDot1agCfmMepMgmtSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepMgmtSdpId.setStatus("current")
_TmnxDot1agCfmMepMgmtVcId_Type = Unsigned32
_TmnxDot1agCfmMepMgmtVcId_Object = MibTableColumn
tmnxDot1agCfmMepMgmtVcId = _TmnxDot1agCfmMepMgmtVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 3, 1, 1, 7),
    _TmnxDot1agCfmMepMgmtVcId_Type()
)
tmnxDot1agCfmMepMgmtVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepMgmtVcId.setStatus("current")
_TmnxDot1agCfmMepMgmtFcltyIfIndex_Type = InterfaceIndexOrZero
_TmnxDot1agCfmMepMgmtFcltyIfIndex_Object = MibTableColumn
tmnxDot1agCfmMepMgmtFcltyIfIndex = _TmnxDot1agCfmMepMgmtFcltyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 3, 1, 1, 8),
    _TmnxDot1agCfmMepMgmtFcltyIfIndex_Type()
)
tmnxDot1agCfmMepMgmtFcltyIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepMgmtFcltyIfIndex.setStatus("current")
_TmnxDot1agCfmMepMgmtFcltyVlanId_Type = VlanIdOrNone
_TmnxDot1agCfmMepMgmtFcltyVlanId_Object = MibTableColumn
tmnxDot1agCfmMepMgmtFcltyVlanId = _TmnxDot1agCfmMepMgmtFcltyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 3, 1, 1, 9),
    _TmnxDot1agCfmMepMgmtFcltyVlanId_Type()
)
tmnxDot1agCfmMepMgmtFcltyVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepMgmtFcltyVlanId.setStatus("current")


class _TmnxDot1agCfmMepMgmtDirection_Type(Dot1agCfmMpDirection):
    """Custom type tmnxDot1agCfmMepMgmtDirection based on Dot1agCfmMpDirection"""
    defaultValue = 1


_TmnxDot1agCfmMepMgmtDirection_Type.__name__ = "Dot1agCfmMpDirection"
_TmnxDot1agCfmMepMgmtDirection_Object = MibTableColumn
tmnxDot1agCfmMepMgmtDirection = _TmnxDot1agCfmMepMgmtDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 3, 1, 1, 50),
    _TmnxDot1agCfmMepMgmtDirection_Type()
)
tmnxDot1agCfmMepMgmtDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepMgmtDirection.setStatus("current")
_TmnxDot1agCfmMd_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmMd = _TmnxDot1agCfmMd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 5)
)
_TmnxDot1agCfmMdTable_Object = MibTable
tmnxDot1agCfmMdTable = _TmnxDot1agCfmMdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMdTable.setStatus("current")
_TmnxDot1agCfmMdEntry_Object = MibTableRow
tmnxDot1agCfmMdEntry = _TmnxDot1agCfmMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 5, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMdEntry.setStatus("current")
_TmnxDot1agCfmMdCreationOrigin_Type = TmnxCreateOrigin
_TmnxDot1agCfmMdCreationOrigin_Object = MibTableColumn
tmnxDot1agCfmMdCreationOrigin = _TmnxDot1agCfmMdCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 5, 1, 1, 1),
    _TmnxDot1agCfmMdCreationOrigin_Type()
)
tmnxDot1agCfmMdCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMdCreationOrigin.setStatus("current")
_TmnxDot1agCfmMa_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmMa = _TmnxDot1agCfmMa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 6)
)
_TmnxDot1agCfmMaNetTable_Object = MibTable
tmnxDot1agCfmMaNetTable = _TmnxDot1agCfmMaNetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaNetTable.setStatus("current")
_TmnxDot1agCfmMaNetEntry_Object = MibTableRow
tmnxDot1agCfmMaNetEntry = _TmnxDot1agCfmMaNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 6, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaNetEntry.setStatus("current")


class _TmnxDot1agCfmMaNetHoldDownTimer_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMaNetHoldDownTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_TmnxDot1agCfmMaNetHoldDownTimer_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMaNetHoldDownTimer_Object = MibTableColumn
tmnxDot1agCfmMaNetHoldDownTimer = _TmnxDot1agCfmMaNetHoldDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 6, 1, 1, 1),
    _TmnxDot1agCfmMaNetHoldDownTimer_Type()
)
tmnxDot1agCfmMaNetHoldDownTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaNetHoldDownTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaNetHoldDownTimer.setUnits("centiseconds")
_TmnxDot1agCfmMaNetTotalMEPCount_Type = Counter32
_TmnxDot1agCfmMaNetTotalMEPCount_Object = MibTableColumn
tmnxDot1agCfmMaNetTotalMEPCount = _TmnxDot1agCfmMaNetTotalMEPCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 6, 1, 1, 2),
    _TmnxDot1agCfmMaNetTotalMEPCount_Type()
)
tmnxDot1agCfmMaNetTotalMEPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaNetTotalMEPCount.setStatus("current")


class _TmnxDot1agCfmMaNetAutoDiscAdmin_Type(TruthValue):
    """Custom type tmnxDot1agCfmMaNetAutoDiscAdmin based on TruthValue"""
    defaultValue = 2


_TmnxDot1agCfmMaNetAutoDiscAdmin_Type.__name__ = "TruthValue"
_TmnxDot1agCfmMaNetAutoDiscAdmin_Object = MibTableColumn
tmnxDot1agCfmMaNetAutoDiscAdmin = _TmnxDot1agCfmMaNetAutoDiscAdmin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 6, 1, 1, 3),
    _TmnxDot1agCfmMaNetAutoDiscAdmin_Type()
)
tmnxDot1agCfmMaNetAutoDiscAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaNetAutoDiscAdmin.setStatus("current")


class _TmnxDot1agCfmMaNetIdPermission_Type(Dot1agCfmIdPermission):
    """Custom type tmnxDot1agCfmMaNetIdPermission based on Dot1agCfmIdPermission"""
    defaultValue = 1


_TmnxDot1agCfmMaNetIdPermission_Type.__name__ = "Dot1agCfmIdPermission"
_TmnxDot1agCfmMaNetIdPermission_Object = MibTableColumn
tmnxDot1agCfmMaNetIdPermission = _TmnxDot1agCfmMaNetIdPermission_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 6, 1, 1, 4),
    _TmnxDot1agCfmMaNetIdPermission_Type()
)
tmnxDot1agCfmMaNetIdPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaNetIdPermission.setStatus("current")
_TmnxDot1agCfmMaCompTable_Object = MibTable
tmnxDot1agCfmMaCompTable = _TmnxDot1agCfmMaCompTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 6, 2)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaCompTable.setStatus("current")
_TmnxDot1agCfmMaCompEntry_Object = MibTableRow
tmnxDot1agCfmMaCompEntry = _TmnxDot1agCfmMaCompEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 6, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaCompEntry.setStatus("current")


class _TmnxDot1agCfmMaCompMipLtrPrio_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMaCompMipLtrPrio based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxDot1agCfmMaCompMipLtrPrio_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMaCompMipLtrPrio_Object = MibTableColumn
tmnxDot1agCfmMaCompMipLtrPrio = _TmnxDot1agCfmMaCompMipLtrPrio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 6, 2, 1, 1),
    _TmnxDot1agCfmMaCompMipLtrPrio_Type()
)
tmnxDot1agCfmMaCompMipLtrPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaCompMipLtrPrio.setStatus("current")
_TmnxDot1agCfmMaMepListTable_Object = MibTable
tmnxDot1agCfmMaMepListTable = _TmnxDot1agCfmMaMepListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 6, 3)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaMepListTable.setStatus("current")
_TmnxDot1agCfmMaMepListEntry_Object = MibTableRow
tmnxDot1agCfmMaMepListEntry = _TmnxDot1agCfmMaMepListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 6, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaMepListEntry.setStatus("current")


class _TmnxDot1agCfmMaMepListMacAddress_Type(MacAddress):
    """Custom type tmnxDot1agCfmMaMepListMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxDot1agCfmMaMepListMacAddress_Type.__name__ = "MacAddress"
_TmnxDot1agCfmMaMepListMacAddress_Object = MibTableColumn
tmnxDot1agCfmMaMepListMacAddress = _TmnxDot1agCfmMaMepListMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 6, 3, 1, 1),
    _TmnxDot1agCfmMaMepListMacAddress_Type()
)
tmnxDot1agCfmMaMepListMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaMepListMacAddress.setStatus("current")


class _TmnxDot1agCfmMaMepListAutoDiscvd_Type(TruthValue):
    """Custom type tmnxDot1agCfmMaMepListAutoDiscvd based on TruthValue"""
    defaultValue = 2


_TmnxDot1agCfmMaMepListAutoDiscvd_Type.__name__ = "TruthValue"
_TmnxDot1agCfmMaMepListAutoDiscvd_Object = MibTableColumn
tmnxDot1agCfmMaMepListAutoDiscvd = _TmnxDot1agCfmMaMepListAutoDiscvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 6, 3, 1, 2),
    _TmnxDot1agCfmMaMepListAutoDiscvd_Type()
)
tmnxDot1agCfmMaMepListAutoDiscvd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaMepListAutoDiscvd.setStatus("current")
_TmnxDot1agCfmMep_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmMep = _TmnxDot1agCfmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7)
)
_TmnxDot1agCfmMepTable_Object = MibTable
tmnxDot1agCfmMepTable = _TmnxDot1agCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepTable.setStatus("current")
_TmnxDot1agCfmMepEntry_Object = MibTableRow
tmnxDot1agCfmMepEntry = _TmnxDot1agCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepEntry.setStatus("current")
_TmnxDot1agCfmMepSdpId_Type = SdpId
_TmnxDot1agCfmMepSdpId_Object = MibTableColumn
tmnxDot1agCfmMepSdpId = _TmnxDot1agCfmMepSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 1),
    _TmnxDot1agCfmMepSdpId_Type()
)
tmnxDot1agCfmMepSdpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSdpId.setStatus("current")
_TmnxDot1agCfmMepVcId_Type = Unsigned32
_TmnxDot1agCfmMepVcId_Object = MibTableColumn
tmnxDot1agCfmMepVcId = _TmnxDot1agCfmMepVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 2),
    _TmnxDot1agCfmMepVcId_Type()
)
tmnxDot1agCfmMepVcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepVcId.setStatus("current")
_TmnxDot1agCfmMepMacAddress_Type = MacAddress
_TmnxDot1agCfmMepMacAddress_Object = MibTableColumn
tmnxDot1agCfmMepMacAddress = _TmnxDot1agCfmMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 3),
    _TmnxDot1agCfmMepMacAddress_Type()
)
tmnxDot1agCfmMepMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepMacAddress.setStatus("current")


class _TmnxDot1agCfmMepAisEnable_Type(TruthValue):
    """Custom type tmnxDot1agCfmMepAisEnable based on TruthValue"""
    defaultValue = 2


_TmnxDot1agCfmMepAisEnable_Type.__name__ = "TruthValue"
_TmnxDot1agCfmMepAisEnable_Object = MibTableColumn
tmnxDot1agCfmMepAisEnable = _TmnxDot1agCfmMepAisEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 4),
    _TmnxDot1agCfmMepAisEnable_Type()
)
tmnxDot1agCfmMepAisEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepAisEnable.setStatus("current")


class _TmnxDot1agCfmMepAisMegLevel_Type(Bits):
    """Custom type tmnxDot1agCfmMepAisMegLevel based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("level1", 0),
          ("level2", 1),
          ("level3", 2),
          ("level4", 3),
          ("level5", 4),
          ("level6", 5),
          ("level7", 6))
    )

_TmnxDot1agCfmMepAisMegLevel_Type.__name__ = "Bits"
_TmnxDot1agCfmMepAisMegLevel_Object = MibTableColumn
tmnxDot1agCfmMepAisMegLevel = _TmnxDot1agCfmMepAisMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 5),
    _TmnxDot1agCfmMepAisMegLevel_Type()
)
tmnxDot1agCfmMepAisMegLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepAisMegLevel.setStatus("current")


class _TmnxDot1agCfmMepAisPriority_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepAisPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxDot1agCfmMepAisPriority_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepAisPriority_Object = MibTableColumn
tmnxDot1agCfmMepAisPriority = _TmnxDot1agCfmMepAisPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 6),
    _TmnxDot1agCfmMepAisPriority_Type()
)
tmnxDot1agCfmMepAisPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepAisPriority.setStatus("current")


class _TmnxDot1agCfmMepAisInterval_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepAisInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(60, 60),
    )


_TmnxDot1agCfmMepAisInterval_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepAisInterval_Object = MibTableColumn
tmnxDot1agCfmMepAisInterval = _TmnxDot1agCfmMepAisInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 7),
    _TmnxDot1agCfmMepAisInterval_Type()
)
tmnxDot1agCfmMepAisInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepAisInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepAisInterval.setUnits("seconds")


class _TmnxDot1agCfmMepEthRxAisInterval_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepEthRxAisInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(60, 60),
    )


_TmnxDot1agCfmMepEthRxAisInterval_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepEthRxAisInterval_Object = MibTableColumn
tmnxDot1agCfmMepEthRxAisInterval = _TmnxDot1agCfmMepEthRxAisInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 8),
    _TmnxDot1agCfmMepEthRxAisInterval_Type()
)
tmnxDot1agCfmMepEthRxAisInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepEthRxAisInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepEthRxAisInterval.setUnits("seconds")


class _TmnxDot1agCfmMepEthRxAis_Type(TruthValue):
    """Custom type tmnxDot1agCfmMepEthRxAis based on TruthValue"""
    defaultValue = 2


_TmnxDot1agCfmMepEthRxAis_Type.__name__ = "TruthValue"
_TmnxDot1agCfmMepEthRxAis_Object = MibTableColumn
tmnxDot1agCfmMepEthRxAis = _TmnxDot1agCfmMepEthRxAis_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 9),
    _TmnxDot1agCfmMepEthRxAis_Type()
)
tmnxDot1agCfmMepEthRxAis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepEthRxAis.setStatus("current")
_TmnxDot1agCfmMepEthAisTxCount_Type = Counter32
_TmnxDot1agCfmMepEthAisTxCount_Object = MibTableColumn
tmnxDot1agCfmMepEthAisTxCount = _TmnxDot1agCfmMepEthAisTxCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 10),
    _TmnxDot1agCfmMepEthAisTxCount_Type()
)
tmnxDot1agCfmMepEthAisTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepEthAisTxCount.setStatus("current")


class _TmnxDot1agCfmMepEthTestEnable_Type(TruthValue):
    """Custom type tmnxDot1agCfmMepEthTestEnable based on TruthValue"""
    defaultValue = 2


_TmnxDot1agCfmMepEthTestEnable_Type.__name__ = "TruthValue"
_TmnxDot1agCfmMepEthTestEnable_Object = MibTableColumn
tmnxDot1agCfmMepEthTestEnable = _TmnxDot1agCfmMepEthTestEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 11),
    _TmnxDot1agCfmMepEthTestEnable_Type()
)
tmnxDot1agCfmMepEthTestEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepEthTestEnable.setStatus("current")


class _TmnxDot1agCfmMepEthTestPattern_Type(Integer32):
    """Custom type tmnxDot1agCfmMepEthTestPattern based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("allZerosNoCrc", 0),
          ("allZerosCrc", 1),
          ("prbsNoCrc", 2),
          ("prbsCrc", 3),
          ("allOnesNoCrc", 4),
          ("allOnesCrc", 5))
    )


_TmnxDot1agCfmMepEthTestPattern_Type.__name__ = "Integer32"
_TmnxDot1agCfmMepEthTestPattern_Object = MibTableColumn
tmnxDot1agCfmMepEthTestPattern = _TmnxDot1agCfmMepEthTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 12),
    _TmnxDot1agCfmMepEthTestPattern_Type()
)
tmnxDot1agCfmMepEthTestPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepEthTestPattern.setStatus("current")


class _TmnxDot1agCfmMepEthTestMacAddr_Type(MacAddress):
    """Custom type tmnxDot1agCfmMepEthTestMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxDot1agCfmMepEthTestMacAddr_Type.__name__ = "MacAddress"
_TmnxDot1agCfmMepEthTestMacAddr_Object = MibTableColumn
tmnxDot1agCfmMepEthTestMacAddr = _TmnxDot1agCfmMepEthTestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 13),
    _TmnxDot1agCfmMepEthTestMacAddr_Type()
)
tmnxDot1agCfmMepEthTestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepEthTestMacAddr.setStatus("current")


class _TmnxDot1agCfmMepEthTestDataLen_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepEthTestDataLen based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_TmnxDot1agCfmMepEthTestDataLen_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepEthTestDataLen_Object = MibTableColumn
tmnxDot1agCfmMepEthTestDataLen = _TmnxDot1agCfmMepEthTestDataLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 14),
    _TmnxDot1agCfmMepEthTestDataLen_Type()
)
tmnxDot1agCfmMepEthTestDataLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepEthTestDataLen.setStatus("current")


class _TmnxDot1agCfmMepEthTestPriority_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepEthTestPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxDot1agCfmMepEthTestPriority_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepEthTestPriority_Object = MibTableColumn
tmnxDot1agCfmMepEthTestPriority = _TmnxDot1agCfmMepEthTestPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 15),
    _TmnxDot1agCfmMepEthTestPriority_Type()
)
tmnxDot1agCfmMepEthTestPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepEthTestPriority.setStatus("current")


class _TmnxDot1agCfmMepOWDTMacAddress_Type(MacAddress):
    """Custom type tmnxDot1agCfmMepOWDTMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxDot1agCfmMepOWDTMacAddress_Type.__name__ = "MacAddress"
_TmnxDot1agCfmMepOWDTMacAddress_Object = MibTableColumn
tmnxDot1agCfmMepOWDTMacAddress = _TmnxDot1agCfmMepOWDTMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 16),
    _TmnxDot1agCfmMepOWDTMacAddress_Type()
)
tmnxDot1agCfmMepOWDTMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepOWDTMacAddress.setStatus("current")


class _TmnxDot1agCfmMepOWDTPriority_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepOWDTPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxDot1agCfmMepOWDTPriority_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepOWDTPriority_Object = MibTableColumn
tmnxDot1agCfmMepOWDTPriority = _TmnxDot1agCfmMepOWDTPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 17),
    _TmnxDot1agCfmMepOWDTPriority_Type()
)
tmnxDot1agCfmMepOWDTPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepOWDTPriority.setStatus("current")


class _TmnxDot1agCfmMepTWDTMacAddress_Type(MacAddress):
    """Custom type tmnxDot1agCfmMepTWDTMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxDot1agCfmMepTWDTMacAddress_Type.__name__ = "MacAddress"
_TmnxDot1agCfmMepTWDTMacAddress_Object = MibTableColumn
tmnxDot1agCfmMepTWDTMacAddress = _TmnxDot1agCfmMepTWDTMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 18),
    _TmnxDot1agCfmMepTWDTMacAddress_Type()
)
tmnxDot1agCfmMepTWDTMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepTWDTMacAddress.setStatus("current")


class _TmnxDot1agCfmMepTWDTPriority_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepTWDTPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxDot1agCfmMepTWDTPriority_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepTWDTPriority_Object = MibTableColumn
tmnxDot1agCfmMepTWDTPriority = _TmnxDot1agCfmMepTWDTPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 19),
    _TmnxDot1agCfmMepTWDTPriority_Type()
)
tmnxDot1agCfmMepTWDTPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepTWDTPriority.setStatus("current")
_TmnxDot1agCfmMepSvcId_Type = TmnxServId
_TmnxDot1agCfmMepSvcId_Object = MibTableColumn
tmnxDot1agCfmMepSvcId = _TmnxDot1agCfmMepSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 20),
    _TmnxDot1agCfmMepSvcId_Type()
)
tmnxDot1agCfmMepSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSvcId.setStatus("current")


class _TmnxDot1agCfmMepControlMep_Type(TruthValue):
    """Custom type tmnxDot1agCfmMepControlMep based on TruthValue"""
    defaultValue = 2


_TmnxDot1agCfmMepControlMep_Type.__name__ = "TruthValue"
_TmnxDot1agCfmMepControlMep_Object = MibTableColumn
tmnxDot1agCfmMepControlMep = _TmnxDot1agCfmMepControlMep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 21),
    _TmnxDot1agCfmMepControlMep_Type()
)
tmnxDot1agCfmMepControlMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepControlMep.setStatus("current")


class _TmnxDot1agCfmMepEthTestThreshold_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepEthTestThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11840),
    )


_TmnxDot1agCfmMepEthTestThreshold_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepEthTestThreshold_Object = MibTableColumn
tmnxDot1agCfmMepEthTestThreshold = _TmnxDot1agCfmMepEthTestThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 22),
    _TmnxDot1agCfmMepEthTestThreshold_Type()
)
tmnxDot1agCfmMepEthTestThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepEthTestThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepEthTestThreshold.setUnits("bit-errors")


class _TmnxDot1agCfmMepOWDTThreshold_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepOWDTThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_TmnxDot1agCfmMepOWDTThreshold_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepOWDTThreshold_Object = MibTableColumn
tmnxDot1agCfmMepOWDTThreshold = _TmnxDot1agCfmMepOWDTThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 23),
    _TmnxDot1agCfmMepOWDTThreshold_Type()
)
tmnxDot1agCfmMepOWDTThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepOWDTThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepOWDTThreshold.setUnits("seconds")


class _TmnxDot1agCfmMepFaultPropagation_Type(Integer32):
    """Custom type tmnxDot1agCfmMepFaultPropagation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("useIfStatusTLV", 1),
          ("suspendCCM", 2))
    )


_TmnxDot1agCfmMepFaultPropagation_Type.__name__ = "Integer32"
_TmnxDot1agCfmMepFaultPropagation_Object = MibTableColumn
tmnxDot1agCfmMepFaultPropagation = _TmnxDot1agCfmMepFaultPropagation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 24),
    _TmnxDot1agCfmMepFaultPropagation_Type()
)
tmnxDot1agCfmMepFaultPropagation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepFaultPropagation.setStatus("current")


class _TmnxDot1agCfmMepFacilityIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tmnxDot1agCfmMepFacilityIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TmnxDot1agCfmMepFacilityIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TmnxDot1agCfmMepFacilityIfIndex_Object = MibTableColumn
tmnxDot1agCfmMepFacilityIfIndex = _TmnxDot1agCfmMepFacilityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 25),
    _TmnxDot1agCfmMepFacilityIfIndex_Type()
)
tmnxDot1agCfmMepFacilityIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepFacilityIfIndex.setStatus("current")


class _TmnxDot1agCfmMepFacilityVlanId_Type(VlanIdOrNone):
    """Custom type tmnxDot1agCfmMepFacilityVlanId based on VlanIdOrNone"""
    defaultValue = 0


_TmnxDot1agCfmMepFacilityVlanId_Type.__name__ = "VlanIdOrNone"
_TmnxDot1agCfmMepFacilityVlanId_Object = MibTableColumn
tmnxDot1agCfmMepFacilityVlanId = _TmnxDot1agCfmMepFacilityVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 26),
    _TmnxDot1agCfmMepFacilityVlanId_Type()
)
tmnxDot1agCfmMepFacilityVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepFacilityVlanId.setStatus("current")


class _TmnxDot1agCfmMepFacilityType_Type(Integer32):
    """Custom type tmnxDot1agCfmMepFacilityType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonFacilityType", 0),
          ("port", 1),
          ("interface", 2))
    )


_TmnxDot1agCfmMepFacilityType_Type.__name__ = "Integer32"
_TmnxDot1agCfmMepFacilityType_Object = MibTableColumn
tmnxDot1agCfmMepFacilityType = _TmnxDot1agCfmMepFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 27),
    _TmnxDot1agCfmMepFacilityType_Type()
)
tmnxDot1agCfmMepFacilityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepFacilityType.setStatus("current")


class _TmnxDot1agCfmMepFcltyFaultNotify_Type(TruthValue):
    """Custom type tmnxDot1agCfmMepFcltyFaultNotify based on TruthValue"""
    defaultValue = 2


_TmnxDot1agCfmMepFcltyFaultNotify_Type.__name__ = "TruthValue"
_TmnxDot1agCfmMepFcltyFaultNotify_Object = MibTableColumn
tmnxDot1agCfmMepFcltyFaultNotify = _TmnxDot1agCfmMepFcltyFaultNotify_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 28),
    _TmnxDot1agCfmMepFcltyFaultNotify_Type()
)
tmnxDot1agCfmMepFcltyFaultNotify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepFcltyFaultNotify.setStatus("current")


class _TmnxDot1agCfmMepDescription_Type(TItemDescription):
    """Custom type tmnxDot1agCfmMepDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxDot1agCfmMepDescription_Type.__name__ = "TItemDescription"
_TmnxDot1agCfmMepDescription_Object = MibTableColumn
tmnxDot1agCfmMepDescription = _TmnxDot1agCfmMepDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 29),
    _TmnxDot1agCfmMepDescription_Type()
)
tmnxDot1agCfmMepDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepDescription.setStatus("current")


class _TmnxDot1agCfmMepMcLagInactive_Type(Integer32):
    """Custom type tmnxDot1agCfmMepMcLagInactive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("standby", 1),
          ("active", 2))
    )


_TmnxDot1agCfmMepMcLagInactive_Type.__name__ = "Integer32"
_TmnxDot1agCfmMepMcLagInactive_Object = MibTableColumn
tmnxDot1agCfmMepMcLagInactive = _TmnxDot1agCfmMepMcLagInactive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 30),
    _TmnxDot1agCfmMepMcLagInactive_Type()
)
tmnxDot1agCfmMepMcLagInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepMcLagInactive.setStatus("current")


class _TmnxDot1agCfmMepCcmPaddingSize_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepCcmPaddingSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 1500),
    )


_TmnxDot1agCfmMepCcmPaddingSize_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepCcmPaddingSize_Object = MibTableColumn
tmnxDot1agCfmMepCcmPaddingSize = _TmnxDot1agCfmMepCcmPaddingSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 31),
    _TmnxDot1agCfmMepCcmPaddingSize_Type()
)
tmnxDot1agCfmMepCcmPaddingSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepCcmPaddingSize.setStatus("current")


class _TmnxDot1agCfmMepCcmIgnoreTLVs_Type(Bits):
    """Custom type tmnxDot1agCfmMepCcmIgnoreTLVs based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("interfaceStatus", 0),
          ("portStatus", 1))
    )

_TmnxDot1agCfmMepCcmIgnoreTLVs_Type.__name__ = "Bits"
_TmnxDot1agCfmMepCcmIgnoreTLVs_Object = MibTableColumn
tmnxDot1agCfmMepCcmIgnoreTLVs = _TmnxDot1agCfmMepCcmIgnoreTLVs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 32),
    _TmnxDot1agCfmMepCcmIgnoreTLVs_Type()
)
tmnxDot1agCfmMepCcmIgnoreTLVs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepCcmIgnoreTLVs.setStatus("current")


class _TmnxDot1agCfmMepCsfEnable_Type(TruthValue):
    """Custom type tmnxDot1agCfmMepCsfEnable based on TruthValue"""
    defaultValue = 2


_TmnxDot1agCfmMepCsfEnable_Type.__name__ = "TruthValue"
_TmnxDot1agCfmMepCsfEnable_Object = MibTableColumn
tmnxDot1agCfmMepCsfEnable = _TmnxDot1agCfmMepCsfEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 33),
    _TmnxDot1agCfmMepCsfEnable_Type()
)
tmnxDot1agCfmMepCsfEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepCsfEnable.setStatus("current")


class _TmnxDot1agCfmMepCsfRxMultiplier_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepCsfRxMultiplier based on Unsigned32"""
    defaultValue = 35

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(20, 300),
    )


_TmnxDot1agCfmMepCsfRxMultiplier_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepCsfRxMultiplier_Object = MibTableColumn
tmnxDot1agCfmMepCsfRxMultiplier = _TmnxDot1agCfmMepCsfRxMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 34),
    _TmnxDot1agCfmMepCsfRxMultiplier_Type()
)
tmnxDot1agCfmMepCsfRxMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepCsfRxMultiplier.setStatus("current")


class _TmnxDot1agCfmMepCsfRxState_Type(Integer32):
    """Custom type tmnxDot1agCfmMepCsfRxState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("los", 0),
          ("ais", 1),
          ("rdi", 2),
          ("dci", 3))
    )


_TmnxDot1agCfmMepCsfRxState_Type.__name__ = "Integer32"
_TmnxDot1agCfmMepCsfRxState_Object = MibTableColumn
tmnxDot1agCfmMepCsfRxState = _TmnxDot1agCfmMepCsfRxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 35),
    _TmnxDot1agCfmMepCsfRxState_Type()
)
tmnxDot1agCfmMepCsfRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepCsfRxState.setStatus("current")


class _TmnxDot1agCfmMepCsfRxInterval_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepCsfRxInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(60, 60),
    )


_TmnxDot1agCfmMepCsfRxInterval_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepCsfRxInterval_Object = MibTableColumn
tmnxDot1agCfmMepCsfRxInterval = _TmnxDot1agCfmMepCsfRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 36),
    _TmnxDot1agCfmMepCsfRxInterval_Type()
)
tmnxDot1agCfmMepCsfRxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepCsfRxInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepCsfRxInterval.setUnits("seconds")
_TmnxDot1agCfmMepCsfRxCount_Type = Counter32
_TmnxDot1agCfmMepCsfRxCount_Object = MibTableColumn
tmnxDot1agCfmMepCsfRxCount = _TmnxDot1agCfmMepCsfRxCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 37),
    _TmnxDot1agCfmMepCsfRxCount_Type()
)
tmnxDot1agCfmMepCsfRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepCsfRxCount.setStatus("current")
_TmnxDot1agCfmMepEthAisTxFail_Type = Counter32
_TmnxDot1agCfmMepEthAisTxFail_Object = MibTableColumn
tmnxDot1agCfmMepEthAisTxFail = _TmnxDot1agCfmMepEthAisTxFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 38),
    _TmnxDot1agCfmMepEthAisTxFail_Type()
)
tmnxDot1agCfmMepEthAisTxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepEthAisTxFail.setStatus("current")


class _TmnxDot1agCfmMepTxLbmTimeout_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepTxLbmTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxDot1agCfmMepTxLbmTimeout_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepTxLbmTimeout_Object = MibTableColumn
tmnxDot1agCfmMepTxLbmTimeout = _TmnxDot1agCfmMepTxLbmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 39),
    _TmnxDot1agCfmMepTxLbmTimeout_Type()
)
tmnxDot1agCfmMepTxLbmTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepTxLbmTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepTxLbmTimeout.setUnits("seconds")


class _TmnxDot1agCfmMepTxLbmInterval_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepTxLbmInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 600),
    )


_TmnxDot1agCfmMepTxLbmInterval_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepTxLbmInterval_Object = MibTableColumn
tmnxDot1agCfmMepTxLbmInterval = _TmnxDot1agCfmMepTxLbmInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 40),
    _TmnxDot1agCfmMepTxLbmInterval_Type()
)
tmnxDot1agCfmMepTxLbmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepTxLbmInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepTxLbmInterval.setUnits("centiseconds")


class _TmnxDot1agCfmMepLbmPaddingSize_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepLbmPaddingSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 9000),
    )


_TmnxDot1agCfmMepLbmPaddingSize_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepLbmPaddingSize_Object = MibTableColumn
tmnxDot1agCfmMepLbmPaddingSize = _TmnxDot1agCfmMepLbmPaddingSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 41),
    _TmnxDot1agCfmMepLbmPaddingSize_Type()
)
tmnxDot1agCfmMepLbmPaddingSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepLbmPaddingSize.setStatus("current")


class _TmnxDot1agCfmMepIfSupportEnable_Type(TruthValue):
    """Custom type tmnxDot1agCfmMepIfSupportEnable based on TruthValue"""
    defaultValue = 2


_TmnxDot1agCfmMepIfSupportEnable_Type.__name__ = "TruthValue"
_TmnxDot1agCfmMepIfSupportEnable_Object = MibTableColumn
tmnxDot1agCfmMepIfSupportEnable = _TmnxDot1agCfmMepIfSupportEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 42),
    _TmnxDot1agCfmMepIfSupportEnable_Type()
)
tmnxDot1agCfmMepIfSupportEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepIfSupportEnable.setStatus("current")


class _TmnxDot1agCfmMepAisLowPrioDef_Type(Dot1agCfmLowestAlarmPri):
    """Custom type tmnxDot1agCfmMepAisLowPrioDef based on Dot1agCfmLowestAlarmPri"""
    defaultValue = 1


_TmnxDot1agCfmMepAisLowPrioDef_Type.__name__ = "Dot1agCfmLowestAlarmPri"
_TmnxDot1agCfmMepAisLowPrioDef_Object = MibTableColumn
tmnxDot1agCfmMepAisLowPrioDef = _TmnxDot1agCfmMepAisLowPrioDef_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 1, 1, 43),
    _TmnxDot1agCfmMepAisLowPrioDef_Type()
)
tmnxDot1agCfmMepAisLowPrioDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepAisLowPrioDef.setStatus("current")
_TmnxDot1agCfmMepEthTestRsltTable_Object = MibTable
tmnxDot1agCfmMepEthTestRsltTable = _TmnxDot1agCfmMepEthTestRsltTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 2)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepEthTestRsltTable.setStatus("current")
_TmnxDot1agCfmMepEthTestRsltEntry_Object = MibTableRow
tmnxDot1agCfmMepEthTestRsltEntry = _TmnxDot1agCfmMepEthTestRsltEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 2, 1)
)
tmnxDot1agCfmMepEthTestRsltEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSrcMacAddress"),
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepEthTestRsltEntry.setStatus("current")
_TmnxDot1agCfmMepSrcMacAddress_Type = MacAddress
_TmnxDot1agCfmMepSrcMacAddress_Object = MibTableColumn
tmnxDot1agCfmMepSrcMacAddress = _TmnxDot1agCfmMepSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 2, 1, 1),
    _TmnxDot1agCfmMepSrcMacAddress_Type()
)
tmnxDot1agCfmMepSrcMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSrcMacAddress.setStatus("current")
_TmnxDot1agCfmMepFrameCount_Type = Counter32
_TmnxDot1agCfmMepFrameCount_Object = MibTableColumn
tmnxDot1agCfmMepFrameCount = _TmnxDot1agCfmMepFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 2, 1, 2),
    _TmnxDot1agCfmMepFrameCount_Type()
)
tmnxDot1agCfmMepFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepFrameCount.setStatus("current")
_TmnxDot1agCfmMepByteCount_Type = Counter32
_TmnxDot1agCfmMepByteCount_Object = MibTableColumn
tmnxDot1agCfmMepByteCount = _TmnxDot1agCfmMepByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 2, 1, 3),
    _TmnxDot1agCfmMepByteCount_Type()
)
tmnxDot1agCfmMepByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepByteCount.setStatus("current")
_TmnxDot1agCfmMepFailedBits_Type = Counter32
_TmnxDot1agCfmMepFailedBits_Object = MibTableColumn
tmnxDot1agCfmMepFailedBits = _TmnxDot1agCfmMepFailedBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 2, 1, 4),
    _TmnxDot1agCfmMepFailedBits_Type()
)
tmnxDot1agCfmMepFailedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepFailedBits.setStatus("current")
_TmnxDot1agCfmMepCrcFailures_Type = Counter32
_TmnxDot1agCfmMepCrcFailures_Object = MibTableColumn
tmnxDot1agCfmMepCrcFailures = _TmnxDot1agCfmMepCrcFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 2, 1, 5),
    _TmnxDot1agCfmMepCrcFailures_Type()
)
tmnxDot1agCfmMepCrcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepCrcFailures.setStatus("current")
_TmnxDot1agCfmMepCurrByteCount_Type = Gauge32
_TmnxDot1agCfmMepCurrByteCount_Object = MibTableColumn
tmnxDot1agCfmMepCurrByteCount = _TmnxDot1agCfmMepCurrByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 2, 1, 6),
    _TmnxDot1agCfmMepCurrByteCount_Type()
)
tmnxDot1agCfmMepCurrByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepCurrByteCount.setStatus("current")
_TmnxDot1agCfmMepCurrFailedBits_Type = Gauge32
_TmnxDot1agCfmMepCurrFailedBits_Object = MibTableColumn
tmnxDot1agCfmMepCurrFailedBits = _TmnxDot1agCfmMepCurrFailedBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 2, 1, 7),
    _TmnxDot1agCfmMepCurrFailedBits_Type()
)
tmnxDot1agCfmMepCurrFailedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepCurrFailedBits.setStatus("current")
_TmnxDot1agCfmMepCurrCrcFailures_Type = TruthValue
_TmnxDot1agCfmMepCurrCrcFailures_Object = MibTableColumn
tmnxDot1agCfmMepCurrCrcFailures = _TmnxDot1agCfmMepCurrCrcFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 2, 1, 8),
    _TmnxDot1agCfmMepCurrCrcFailures_Type()
)
tmnxDot1agCfmMepCurrCrcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepCurrCrcFailures.setStatus("current")
_TmnxDot1agCfmMepDelayRsltTable_Object = MibTable
tmnxDot1agCfmMepDelayRsltTable = _TmnxDot1agCfmMepDelayRsltTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 3)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepDelayRsltTable.setStatus("current")
_TmnxDot1agCfmMepDelayRsltEntry_Object = MibTableRow
tmnxDot1agCfmMepDelayRsltEntry = _TmnxDot1agCfmMepDelayRsltEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 3, 1)
)
tmnxDot1agCfmMepDelayRsltEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepDelaySrcMacAddr"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepDelayTestType"),
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepDelayRsltEntry.setStatus("current")
_TmnxDot1agCfmMepDelaySrcMacAddr_Type = MacAddress
_TmnxDot1agCfmMepDelaySrcMacAddr_Object = MibTableColumn
tmnxDot1agCfmMepDelaySrcMacAddr = _TmnxDot1agCfmMepDelaySrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 3, 1, 1),
    _TmnxDot1agCfmMepDelaySrcMacAddr_Type()
)
tmnxDot1agCfmMepDelaySrcMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepDelaySrcMacAddr.setStatus("current")


class _TmnxDot1agCfmMepDelayTestType_Type(Integer32):
    """Custom type tmnxDot1agCfmMepDelayTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneWayTest", 1),
          ("twoWayTest", 2))
    )


_TmnxDot1agCfmMepDelayTestType_Type.__name__ = "Integer32"
_TmnxDot1agCfmMepDelayTestType_Object = MibTableColumn
tmnxDot1agCfmMepDelayTestType = _TmnxDot1agCfmMepDelayTestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 3, 1, 2),
    _TmnxDot1agCfmMepDelayTestType_Type()
)
tmnxDot1agCfmMepDelayTestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepDelayTestType.setStatus("current")
_TmnxDot1agCfmMepDelayTestDelay_Type = Integer32
_TmnxDot1agCfmMepDelayTestDelay_Object = MibTableColumn
tmnxDot1agCfmMepDelayTestDelay = _TmnxDot1agCfmMepDelayTestDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 3, 1, 3),
    _TmnxDot1agCfmMepDelayTestDelay_Type()
)
tmnxDot1agCfmMepDelayTestDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepDelayTestDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepDelayTestDelay.setUnits("microseconds")
_TmnxDot1agCfmMepDelayVariation_Type = Unsigned32
_TmnxDot1agCfmMepDelayVariation_Object = MibTableColumn
tmnxDot1agCfmMepDelayVariation = _TmnxDot1agCfmMepDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 3, 1, 4),
    _TmnxDot1agCfmMepDelayVariation_Type()
)
tmnxDot1agCfmMepDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepDelayVariation.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepDelayVariation.setUnits("microseconds")
_TmnxDot1agCfmMepSlmTWTestTable_Object = MibTable
tmnxDot1agCfmMepSlmTWTestTable = _TmnxDot1agCfmMepSlmTWTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 4)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTWTestTable.setStatus("current")
_TmnxDot1agCfmMepSlmTWTestEntry_Object = MibTableRow
tmnxDot1agCfmMepSlmTWTestEntry = _TmnxDot1agCfmMepSlmTWTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTWTestEntry.setStatus("current")


class _TmnxDot1agCfmMepSlmTWTestStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxDot1agCfmMepSlmTWTestStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxDot1agCfmMepSlmTWTestStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxDot1agCfmMepSlmTWTestStatus_Object = MibTableColumn
tmnxDot1agCfmMepSlmTWTestStatus = _TmnxDot1agCfmMepSlmTWTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 4, 1, 1),
    _TmnxDot1agCfmMepSlmTWTestStatus_Type()
)
tmnxDot1agCfmMepSlmTWTestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTWTestStatus.setStatus("current")
_TmnxDot1agCfmMepSlmTWTestId_Type = Unsigned32
_TmnxDot1agCfmMepSlmTWTestId_Object = MibTableColumn
tmnxDot1agCfmMepSlmTWTestId = _TmnxDot1agCfmMepSlmTWTestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 4, 1, 2),
    _TmnxDot1agCfmMepSlmTWTestId_Type()
)
tmnxDot1agCfmMepSlmTWTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTWTestId.setStatus("current")


class _TmnxDot1agCfmMepSlmTWMacAddress_Type(MacAddress):
    """Custom type tmnxDot1agCfmMepSlmTWMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxDot1agCfmMepSlmTWMacAddress_Type.__name__ = "MacAddress"
_TmnxDot1agCfmMepSlmTWMacAddress_Object = MibTableColumn
tmnxDot1agCfmMepSlmTWMacAddress = _TmnxDot1agCfmMepSlmTWMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 4, 1, 3),
    _TmnxDot1agCfmMepSlmTWMacAddress_Type()
)
tmnxDot1agCfmMepSlmTWMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTWMacAddress.setStatus("current")


class _TmnxDot1agCfmMepSlmTWPriority_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepSlmTWPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxDot1agCfmMepSlmTWPriority_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepSlmTWPriority_Object = MibTableColumn
tmnxDot1agCfmMepSlmTWPriority = _TmnxDot1agCfmMepSlmTWPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 4, 1, 4),
    _TmnxDot1agCfmMepSlmTWPriority_Type()
)
tmnxDot1agCfmMepSlmTWPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTWPriority.setStatus("current")


class _TmnxDot1agCfmMepSlmTWInterval_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepSlmTWInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_TmnxDot1agCfmMepSlmTWInterval_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepSlmTWInterval_Object = MibTableColumn
tmnxDot1agCfmMepSlmTWInterval = _TmnxDot1agCfmMepSlmTWInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 4, 1, 5),
    _TmnxDot1agCfmMepSlmTWInterval_Type()
)
tmnxDot1agCfmMepSlmTWInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTWInterval.setStatus("current")


class _TmnxDot1agCfmMepSlmTWTimeout_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepSlmTWTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxDot1agCfmMepSlmTWTimeout_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepSlmTWTimeout_Object = MibTableColumn
tmnxDot1agCfmMepSlmTWTimeout = _TmnxDot1agCfmMepSlmTWTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 4, 1, 6),
    _TmnxDot1agCfmMepSlmTWTimeout_Type()
)
tmnxDot1agCfmMepSlmTWTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTWTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTWTimeout.setUnits("seconds")


class _TmnxDot1agCfmMepSlmTWDataSize_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepSlmTWDataSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_TmnxDot1agCfmMepSlmTWDataSize_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepSlmTWDataSize_Object = MibTableColumn
tmnxDot1agCfmMepSlmTWDataSize = _TmnxDot1agCfmMepSlmTWDataSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 4, 1, 7),
    _TmnxDot1agCfmMepSlmTWDataSize_Type()
)
tmnxDot1agCfmMepSlmTWDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTWDataSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTWDataSize.setUnits("bytes")


class _TmnxDot1agCfmMepSlmTWSendCount_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepSlmTWSendCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TmnxDot1agCfmMepSlmTWSendCount_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepSlmTWSendCount_Object = MibTableColumn
tmnxDot1agCfmMepSlmTWSendCount = _TmnxDot1agCfmMepSlmTWSendCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 4, 1, 8),
    _TmnxDot1agCfmMepSlmTWSendCount_Type()
)
tmnxDot1agCfmMepSlmTWSendCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTWSendCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTWSendCount.setUnits("packets")


class _TmnxDot1agCfmMepSlmTWIntrvlUnits_Type(Integer32):
    """Custom type tmnxDot1agCfmMepSlmTWIntrvlUnits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("seconds", 1),
          ("centiseconds", 2))
    )


_TmnxDot1agCfmMepSlmTWIntrvlUnits_Type.__name__ = "Integer32"
_TmnxDot1agCfmMepSlmTWIntrvlUnits_Object = MibTableColumn
tmnxDot1agCfmMepSlmTWIntrvlUnits = _TmnxDot1agCfmMepSlmTWIntrvlUnits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 4, 1, 9),
    _TmnxDot1agCfmMepSlmTWIntrvlUnits_Type()
)
tmnxDot1agCfmMepSlmTWIntrvlUnits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTWIntrvlUnits.setStatus("current")
_TmnxDot1agCfmMepSlmOWTestTable_Object = MibTable
tmnxDot1agCfmMepSlmOWTestTable = _TmnxDot1agCfmMepSlmOWTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 5)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmOWTestTable.setStatus("current")
_TmnxDot1agCfmMepSlmOWTestEntry_Object = MibTableRow
tmnxDot1agCfmMepSlmOWTestEntry = _TmnxDot1agCfmMepSlmOWTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmOWTestEntry.setStatus("current")


class _TmnxDot1agCfmMepSlmOWTestStatus_Type(TmnxEnabledDisabled):
    """Custom type tmnxDot1agCfmMepSlmOWTestStatus based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxDot1agCfmMepSlmOWTestStatus_Type.__name__ = "TmnxEnabledDisabled"
_TmnxDot1agCfmMepSlmOWTestStatus_Object = MibTableColumn
tmnxDot1agCfmMepSlmOWTestStatus = _TmnxDot1agCfmMepSlmOWTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 5, 1, 1),
    _TmnxDot1agCfmMepSlmOWTestStatus_Type()
)
tmnxDot1agCfmMepSlmOWTestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmOWTestStatus.setStatus("current")
_TmnxDot1agCfmMepSlmOWTestId_Type = Unsigned32
_TmnxDot1agCfmMepSlmOWTestId_Object = MibTableColumn
tmnxDot1agCfmMepSlmOWTestId = _TmnxDot1agCfmMepSlmOWTestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 5, 1, 2),
    _TmnxDot1agCfmMepSlmOWTestId_Type()
)
tmnxDot1agCfmMepSlmOWTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmOWTestId.setStatus("current")


class _TmnxDot1agCfmMepSlmOWMacAddress_Type(MacAddress):
    """Custom type tmnxDot1agCfmMepSlmOWMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_TmnxDot1agCfmMepSlmOWMacAddress_Type.__name__ = "MacAddress"
_TmnxDot1agCfmMepSlmOWMacAddress_Object = MibTableColumn
tmnxDot1agCfmMepSlmOWMacAddress = _TmnxDot1agCfmMepSlmOWMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 5, 1, 3),
    _TmnxDot1agCfmMepSlmOWMacAddress_Type()
)
tmnxDot1agCfmMepSlmOWMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmOWMacAddress.setStatus("current")


class _TmnxDot1agCfmMepSlmOWPriority_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepSlmOWPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxDot1agCfmMepSlmOWPriority_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepSlmOWPriority_Object = MibTableColumn
tmnxDot1agCfmMepSlmOWPriority = _TmnxDot1agCfmMepSlmOWPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 5, 1, 4),
    _TmnxDot1agCfmMepSlmOWPriority_Type()
)
tmnxDot1agCfmMepSlmOWPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmOWPriority.setStatus("current")


class _TmnxDot1agCfmMepSlmOWInterval_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepSlmOWInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxDot1agCfmMepSlmOWInterval_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepSlmOWInterval_Object = MibTableColumn
tmnxDot1agCfmMepSlmOWInterval = _TmnxDot1agCfmMepSlmOWInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 5, 1, 5),
    _TmnxDot1agCfmMepSlmOWInterval_Type()
)
tmnxDot1agCfmMepSlmOWInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmOWInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmOWInterval.setUnits("seconds")


class _TmnxDot1agCfmMepSlmOWDataSize_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepSlmOWDataSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_TmnxDot1agCfmMepSlmOWDataSize_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepSlmOWDataSize_Object = MibTableColumn
tmnxDot1agCfmMepSlmOWDataSize = _TmnxDot1agCfmMepSlmOWDataSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 5, 1, 6),
    _TmnxDot1agCfmMepSlmOWDataSize_Type()
)
tmnxDot1agCfmMepSlmOWDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmOWDataSize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmOWDataSize.setUnits("bytes")


class _TmnxDot1agCfmMepSlmOWSendCount_Type(Unsigned32):
    """Custom type tmnxDot1agCfmMepSlmOWSendCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TmnxDot1agCfmMepSlmOWSendCount_Type.__name__ = "Unsigned32"
_TmnxDot1agCfmMepSlmOWSendCount_Object = MibTableColumn
tmnxDot1agCfmMepSlmOWSendCount = _TmnxDot1agCfmMepSlmOWSendCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 5, 1, 7),
    _TmnxDot1agCfmMepSlmOWSendCount_Type()
)
tmnxDot1agCfmMepSlmOWSendCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmOWSendCount.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmOWSendCount.setUnits("packets")
_TmnxDot1agCfmMepSlmTestRsltTable_Object = MibTable
tmnxDot1agCfmMepSlmTestRsltTable = _TmnxDot1agCfmMepSlmTestRsltTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 6)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTestRsltTable.setStatus("current")
_TmnxDot1agCfmMepSlmTestRsltEntry_Object = MibTableRow
tmnxDot1agCfmMepSlmTestRsltEntry = _TmnxDot1agCfmMepSlmTestRsltEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 6, 1)
)
tmnxDot1agCfmMepSlmTestRsltEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmTestType"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmRemoteMacAddr"),
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTestRsltEntry.setStatus("current")


class _TmnxDot1agCfmMepSlmTestType_Type(Integer32):
    """Custom type tmnxDot1agCfmMepSlmTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneWayTest", 1),
          ("twoWayTest", 2))
    )


_TmnxDot1agCfmMepSlmTestType_Type.__name__ = "Integer32"
_TmnxDot1agCfmMepSlmTestType_Object = MibTableColumn
tmnxDot1agCfmMepSlmTestType = _TmnxDot1agCfmMepSlmTestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 6, 1, 1),
    _TmnxDot1agCfmMepSlmTestType_Type()
)
tmnxDot1agCfmMepSlmTestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTestType.setStatus("current")
_TmnxDot1agCfmMepSlmRemoteMacAddr_Type = MacAddress
_TmnxDot1agCfmMepSlmRemoteMacAddr_Object = MibTableColumn
tmnxDot1agCfmMepSlmRemoteMacAddr = _TmnxDot1agCfmMepSlmRemoteMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 6, 1, 2),
    _TmnxDot1agCfmMepSlmRemoteMacAddr_Type()
)
tmnxDot1agCfmMepSlmRemoteMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmRemoteMacAddr.setStatus("current")
_TmnxDot1agCfmMepSlmTestId_Type = Unsigned32
_TmnxDot1agCfmMepSlmTestId_Object = MibTableColumn
tmnxDot1agCfmMepSlmTestId = _TmnxDot1agCfmMepSlmTestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 6, 1, 3),
    _TmnxDot1agCfmMepSlmTestId_Type()
)
tmnxDot1agCfmMepSlmTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTestId.setStatus("current")
_TmnxDot1agCfmMepSlmRemoteMepId_Type = Dot1agCfmMepId
_TmnxDot1agCfmMepSlmRemoteMepId_Object = MibTableColumn
tmnxDot1agCfmMepSlmRemoteMepId = _TmnxDot1agCfmMepSlmRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 6, 1, 4),
    _TmnxDot1agCfmMepSlmRemoteMepId_Type()
)
tmnxDot1agCfmMepSlmRemoteMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmRemoteMepId.setStatus("current")
_TmnxDot1agCfmMepSlmLastTxSeqF_Type = Unsigned32
_TmnxDot1agCfmMepSlmLastTxSeqF_Object = MibTableColumn
tmnxDot1agCfmMepSlmLastTxSeqF = _TmnxDot1agCfmMepSlmLastTxSeqF_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 6, 1, 5),
    _TmnxDot1agCfmMepSlmLastTxSeqF_Type()
)
tmnxDot1agCfmMepSlmLastTxSeqF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmLastTxSeqF.setStatus("current")
_TmnxDot1agCfmMepSlmPacketIn_Type = Counter32
_TmnxDot1agCfmMepSlmPacketIn_Object = MibTableColumn
tmnxDot1agCfmMepSlmPacketIn = _TmnxDot1agCfmMepSlmPacketIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 6, 1, 6),
    _TmnxDot1agCfmMepSlmPacketIn_Type()
)
tmnxDot1agCfmMepSlmPacketIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmPacketIn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmPacketIn.setUnits("packets")
_TmnxDot1agCfmMepSlmPacketLossIn_Type = Integer32
_TmnxDot1agCfmMepSlmPacketLossIn_Object = MibTableColumn
tmnxDot1agCfmMepSlmPacketLossIn = _TmnxDot1agCfmMepSlmPacketLossIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 6, 1, 7),
    _TmnxDot1agCfmMepSlmPacketLossIn_Type()
)
tmnxDot1agCfmMepSlmPacketLossIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmPacketLossIn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmPacketLossIn.setUnits("packets")
_TmnxDot1agCfmMepSlmPacketLossOut_Type = Integer32
_TmnxDot1agCfmMepSlmPacketLossOut_Object = MibTableColumn
tmnxDot1agCfmMepSlmPacketLossOut = _TmnxDot1agCfmMepSlmPacketLossOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 6, 1, 8),
    _TmnxDot1agCfmMepSlmPacketLossOut_Type()
)
tmnxDot1agCfmMepSlmPacketLossOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmPacketLossOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmPacketLossOut.setUnits("packets")
_TmnxDot1agCfmMepSlmPacketUnack_Type = Gauge32
_TmnxDot1agCfmMepSlmPacketUnack_Object = MibTableColumn
tmnxDot1agCfmMepSlmPacketUnack = _TmnxDot1agCfmMepSlmPacketUnack_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 6, 1, 9),
    _TmnxDot1agCfmMepSlmPacketUnack_Type()
)
tmnxDot1agCfmMepSlmPacketUnack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmPacketUnack.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmPacketUnack.setUnits("packets")
_TmnxDot1agCfmMepMcstLbmRsltTable_Object = MibTable
tmnxDot1agCfmMepMcstLbmRsltTable = _TmnxDot1agCfmMepMcstLbmRsltTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 7)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepMcstLbmRsltTable.setStatus("current")
_TmnxDot1agCfmMepMcstLbmRsltEntry_Object = MibTableRow
tmnxDot1agCfmMepMcstLbmRsltEntry = _TmnxDot1agCfmMepMcstLbmRsltEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 7, 1)
)
tmnxDot1agCfmMepMcstLbmRsltEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepLbmRemoteMepMac"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepLbmSeqNumber"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepLbmRxIndex"),
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepMcstLbmRsltEntry.setStatus("current")
_TmnxDot1agCfmMepLbmRemoteMepMac_Type = MacAddress
_TmnxDot1agCfmMepLbmRemoteMepMac_Object = MibTableColumn
tmnxDot1agCfmMepLbmRemoteMepMac = _TmnxDot1agCfmMepLbmRemoteMepMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 7, 1, 1),
    _TmnxDot1agCfmMepLbmRemoteMepMac_Type()
)
tmnxDot1agCfmMepLbmRemoteMepMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepLbmRemoteMepMac.setStatus("current")
_TmnxDot1agCfmMepLbmSeqNumber_Type = Unsigned32
_TmnxDot1agCfmMepLbmSeqNumber_Object = MibTableColumn
tmnxDot1agCfmMepLbmSeqNumber = _TmnxDot1agCfmMepLbmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 7, 1, 2),
    _TmnxDot1agCfmMepLbmSeqNumber_Type()
)
tmnxDot1agCfmMepLbmSeqNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepLbmSeqNumber.setStatus("current")
_TmnxDot1agCfmMepLbmRxIndex_Type = Unsigned32
_TmnxDot1agCfmMepLbmRxIndex_Object = MibTableColumn
tmnxDot1agCfmMepLbmRxIndex = _TmnxDot1agCfmMepLbmRxIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 7, 1, 3),
    _TmnxDot1agCfmMepLbmRxIndex_Type()
)
tmnxDot1agCfmMepLbmRxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepLbmRxIndex.setStatus("current")
_TmnxDot1agCfmMepDbTable_Object = MibTable
tmnxDot1agCfmMepDbTable = _TmnxDot1agCfmMepDbTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 8)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepDbTable.setStatus("current")
_TmnxDot1agCfmMepDbEntry_Object = MibTableRow
tmnxDot1agCfmMepDbEntry = _TmnxDot1agCfmMepDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 8, 1)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepDbEntry.setStatus("current")
_TmnxDot1agCfmMepDbGraceRx_Type = TruthValue
_TmnxDot1agCfmMepDbGraceRx_Object = MibTableColumn
tmnxDot1agCfmMepDbGraceRx = _TmnxDot1agCfmMepDbGraceRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 8, 1, 1),
    _TmnxDot1agCfmMepDbGraceRx_Type()
)
tmnxDot1agCfmMepDbGraceRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepDbGraceRx.setStatus("current")
_TmnxDot1agCfmMepOpcodeTable_Object = MibTable
tmnxDot1agCfmMepOpcodeTable = _TmnxDot1agCfmMepOpcodeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 9)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepOpcodeTable.setStatus("current")
_TmnxDot1agCfmMepOpcodeEntry_Object = MibTableRow
tmnxDot1agCfmMepOpcodeEntry = _TmnxDot1agCfmMepOpcodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 9, 1)
)
tmnxDot1agCfmMepOpcodeEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepOpcode"),
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepOpcodeEntry.setStatus("current")
_TmnxDot1agCfmMepOpcode_Type = Dot1agCfmStatisticOpcodeName
_TmnxDot1agCfmMepOpcode_Object = MibTableColumn
tmnxDot1agCfmMepOpcode = _TmnxDot1agCfmMepOpcode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 9, 1, 1),
    _TmnxDot1agCfmMepOpcode_Type()
)
tmnxDot1agCfmMepOpcode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepOpcode.setStatus("current")
_TmnxDot1agCfmMepOpcodeRx_Type = Counter32
_TmnxDot1agCfmMepOpcodeRx_Object = MibTableColumn
tmnxDot1agCfmMepOpcodeRx = _TmnxDot1agCfmMepOpcodeRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 9, 1, 2),
    _TmnxDot1agCfmMepOpcodeRx_Type()
)
tmnxDot1agCfmMepOpcodeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepOpcodeRx.setStatus("current")
_TmnxDot1agCfmMepOpcodeTx_Type = Counter32
_TmnxDot1agCfmMepOpcodeTx_Object = MibTableColumn
tmnxDot1agCfmMepOpcodeTx = _TmnxDot1agCfmMepOpcodeTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 7, 9, 1, 3),
    _TmnxDot1agCfmMepOpcodeTx_Type()
)
tmnxDot1agCfmMepOpcodeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepOpcodeTx.setStatus("current")
_TmnxDot1agCfmMip_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmMip = _TmnxDot1agCfmMip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 8)
)
_TmnxDot1agCfmSapMipTable_Object = MibTable
tmnxDot1agCfmSapMipTable = _TmnxDot1agCfmSapMipTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 8, 1)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmSapMipTable.setStatus("current")
_TmnxDot1agCfmSapMipEntry_Object = MibTableRow
tmnxDot1agCfmSapMipEntry = _TmnxDot1agCfmSapMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 8, 1, 1)
)
tmnxDot1agCfmSapMipEntry.setIndexNames(
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSapMipIfIndex"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSapMipVlanIdOrNone"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSapMipPrimaryVlanId"),
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmSapMipEntry.setStatus("current")
_TmnxDot1agCfmSapMipIfIndex_Type = InterfaceIndex
_TmnxDot1agCfmSapMipIfIndex_Object = MibTableColumn
tmnxDot1agCfmSapMipIfIndex = _TmnxDot1agCfmSapMipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 8, 1, 1, 1),
    _TmnxDot1agCfmSapMipIfIndex_Type()
)
tmnxDot1agCfmSapMipIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSapMipIfIndex.setStatus("current")
_TmnxDot1agCfmSapMipVlanIdOrNone_Type = Unsigned32
_TmnxDot1agCfmSapMipVlanIdOrNone_Object = MibTableColumn
tmnxDot1agCfmSapMipVlanIdOrNone = _TmnxDot1agCfmSapMipVlanIdOrNone_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 8, 1, 1, 2),
    _TmnxDot1agCfmSapMipVlanIdOrNone_Type()
)
tmnxDot1agCfmSapMipVlanIdOrNone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSapMipVlanIdOrNone.setStatus("current")
_TmnxDot1agCfmSapMipRowStatus_Type = RowStatus
_TmnxDot1agCfmSapMipRowStatus_Object = MibTableColumn
tmnxDot1agCfmSapMipRowStatus = _TmnxDot1agCfmSapMipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 8, 1, 1, 3),
    _TmnxDot1agCfmSapMipRowStatus_Type()
)
tmnxDot1agCfmSapMipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSapMipRowStatus.setStatus("current")
_TmnxDot1agCfmSapMipSrcMacAddress_Type = MacAddress
_TmnxDot1agCfmSapMipSrcMacAddress_Object = MibTableColumn
tmnxDot1agCfmSapMipSrcMacAddress = _TmnxDot1agCfmSapMipSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 8, 1, 1, 4),
    _TmnxDot1agCfmSapMipSrcMacAddress_Type()
)
tmnxDot1agCfmSapMipSrcMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSapMipSrcMacAddress.setStatus("current")
_TmnxDot1agCfmSapMipPrimaryVlanId_Type = VlanIdOrNone
_TmnxDot1agCfmSapMipPrimaryVlanId_Object = MibTableColumn
tmnxDot1agCfmSapMipPrimaryVlanId = _TmnxDot1agCfmSapMipPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 8, 1, 1, 5),
    _TmnxDot1agCfmSapMipPrimaryVlanId_Type()
)
tmnxDot1agCfmSapMipPrimaryVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSapMipPrimaryVlanId.setStatus("current")
_TmnxDot1agCfmSdpMipTable_Object = MibTable
tmnxDot1agCfmSdpMipTable = _TmnxDot1agCfmSdpMipTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 8, 2)
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpMipTable.setStatus("current")
_TmnxDot1agCfmSdpMipEntry_Object = MibTableRow
tmnxDot1agCfmSdpMipEntry = _TmnxDot1agCfmSdpMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 8, 2, 1)
)
tmnxDot1agCfmSdpMipEntry.setIndexNames(
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpMipSvcId"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpMipSdpId"),
    (0, "TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpMipVcId"),
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpMipEntry.setStatus("current")
_TmnxDot1agCfmSdpMipSvcId_Type = TmnxServId
_TmnxDot1agCfmSdpMipSvcId_Object = MibTableColumn
tmnxDot1agCfmSdpMipSvcId = _TmnxDot1agCfmSdpMipSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 8, 2, 1, 1),
    _TmnxDot1agCfmSdpMipSvcId_Type()
)
tmnxDot1agCfmSdpMipSvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpMipSvcId.setStatus("current")
_TmnxDot1agCfmSdpMipSdpId_Type = SdpId
_TmnxDot1agCfmSdpMipSdpId_Object = MibTableColumn
tmnxDot1agCfmSdpMipSdpId = _TmnxDot1agCfmSdpMipSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 8, 2, 1, 2),
    _TmnxDot1agCfmSdpMipSdpId_Type()
)
tmnxDot1agCfmSdpMipSdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpMipSdpId.setStatus("current")
_TmnxDot1agCfmSdpMipVcId_Type = Unsigned32
_TmnxDot1agCfmSdpMipVcId_Object = MibTableColumn
tmnxDot1agCfmSdpMipVcId = _TmnxDot1agCfmSdpMipVcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 8, 2, 1, 3),
    _TmnxDot1agCfmSdpMipVcId_Type()
)
tmnxDot1agCfmSdpMipVcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpMipVcId.setStatus("current")
_TmnxDot1agCfmSdpMipRowStatus_Type = RowStatus
_TmnxDot1agCfmSdpMipRowStatus_Object = MibTableColumn
tmnxDot1agCfmSdpMipRowStatus = _TmnxDot1agCfmSdpMipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 8, 2, 1, 4),
    _TmnxDot1agCfmSdpMipRowStatus_Type()
)
tmnxDot1agCfmSdpMipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpMipRowStatus.setStatus("current")
_TmnxDot1agCfmSdpMipSrcMacAddress_Type = MacAddress
_TmnxDot1agCfmSdpMipSrcMacAddress_Object = MibTableColumn
tmnxDot1agCfmSdpMipSrcMacAddress = _TmnxDot1agCfmSdpMipSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 8, 2, 1, 5),
    _TmnxDot1agCfmSdpMipSrcMacAddress_Type()
)
tmnxDot1agCfmSdpMipSrcMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpMipSrcMacAddress.setStatus("current")
_TmnxDot1agCfmNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxDot1agCfmNotificationObjs = _TmnxDot1agCfmNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 9)
)
_TmnxDot1agCfmNotifySvcId_Type = TmnxServId
_TmnxDot1agCfmNotifySvcId_Object = MibScalar
tmnxDot1agCfmNotifySvcId = _TmnxDot1agCfmNotifySvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 52, 9, 1),
    _TmnxDot1agCfmNotifySvcId_Type()
)
tmnxDot1agCfmNotifySvcId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxDot1agCfmNotifySvcId.setStatus("current")
_TmnxDot1agNotificationsPrefix_ObjectIdentity = ObjectIdentity
tmnxDot1agNotificationsPrefix = _TmnxDot1agNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 52)
)
_TmnxDot1agNotifications_ObjectIdentity = ObjectIdentity
tmnxDot1agNotifications = _TmnxDot1agNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 52, 0)
)
dot1agCfmMepEntry.registerAugmentions(
    ("TIMETRA-IEEE8021-CFM-MIB",
     "tmnxDot1agCfmMepMgmtEntry")
)
tmnxDot1agCfmMepMgmtEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMdEntry.registerAugmentions(
    ("TIMETRA-IEEE8021-CFM-MIB",
     "tmnxDot1agCfmMdEntry")
)
tmnxDot1agCfmMdEntry.setIndexNames(*dot1agCfmMdEntry.getIndexNames())
dot1agCfmMaNetEntry.registerAugmentions(
    ("TIMETRA-IEEE8021-CFM-MIB",
     "tmnxDot1agCfmMaNetEntry")
)
tmnxDot1agCfmMaNetEntry.setIndexNames(*dot1agCfmMaNetEntry.getIndexNames())
dot1agCfmMaCompEntry.registerAugmentions(
    ("TIMETRA-IEEE8021-CFM-MIB",
     "tmnxDot1agCfmMaCompEntry")
)
tmnxDot1agCfmMaCompEntry.setIndexNames(*dot1agCfmMaCompEntry.getIndexNames())
dot1agCfmMaMepListEntry.registerAugmentions(
    ("TIMETRA-IEEE8021-CFM-MIB",
     "tmnxDot1agCfmMaMepListEntry")
)
tmnxDot1agCfmMaMepListEntry.setIndexNames(*dot1agCfmMaMepListEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("TIMETRA-IEEE8021-CFM-MIB",
     "tmnxDot1agCfmMepEntry")
)
tmnxDot1agCfmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("TIMETRA-IEEE8021-CFM-MIB",
     "tmnxDot1agCfmMepSlmTWTestEntry")
)
tmnxDot1agCfmMepSlmTWTestEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("TIMETRA-IEEE8021-CFM-MIB",
     "tmnxDot1agCfmMepSlmOWTestEntry")
)
tmnxDot1agCfmMepSlmOWTestEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMepDbEntry.registerAugmentions(
    ("TIMETRA-IEEE8021-CFM-MIB",
     "tmnxDot1agCfmMepDbEntry")
)
tmnxDot1agCfmMepDbEntry.setIndexNames(*dot1agCfmMepDbEntry.getIndexNames())

# Managed Objects groups

tmnxDot1agCfmSdpBindStackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 1)
)
tmnxDot1agCfmSdpBindStackGroup.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpBindStackMdIndex"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpBindStackMaIndex"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpBindStackMepId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpBindStackMacAddress"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmSdpBindStackGroup.setStatus("current")

tmnxDot1agCfmMepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 2)
)
tmnxDot1agCfmMepGroup.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSdpId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepVcId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepMacAddress"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepGroup.setStatus("obsolete")

tmnxDot1agCfmSapStackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 3)
)
tmnxDot1agCfmSapStackGroup.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmStackMdIndex"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmStackMaIndex"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmStackMepId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmStackMacAddress"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmSapStackGroup.setStatus("current")

tmnxDot1agCfmMipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 5)
)
tmnxDot1agCfmMipGroup.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSapMipRowStatus"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpMipRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMipGroup.setStatus("obsolete")

tmnxDot1agCfmMepGroupV7v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 6)
)
tmnxDot1agCfmMepGroupV7v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSdpId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepVcId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepMacAddress"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepAisEnable"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepAisMegLevel"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepAisPriority"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepAisInterval"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepEthTestEnable"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepEthTestPattern"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepEthRxAisInterval"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepEthRxAis"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepEthAisTxCount"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepEthTestMacAddr"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepEthTestDataLen"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepEthTestPriority"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepOWDTMacAddress"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepOWDTPriority"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepTWDTMacAddress"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepTWDTPriority"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepFrameCount"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepByteCount"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepFailedBits"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCrcFailures"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCurrByteCount"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCurrFailedBits"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCurrCrcFailures"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepDelayTestDelay"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepDelayVariation"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSvcId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepControlMep"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepEthTestThreshold"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepOWDTThreshold"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmVStackMdIndex"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmVStackMaIndex"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmVStackMepId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmVStackMacAddress"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmStackMPType"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepGroupV7v0.setStatus("current")

tmnxDot1agCfmNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 8)
)
tmnxDot1agCfmNotifyObjsGroup.setObjects(
    ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmNotifySvcId")
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmNotifyObjsGroup.setStatus("current")

tmnxDot1agCfmMipGroupV8v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 12, 1)
)
tmnxDot1agCfmMipGroupV8v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSapMipRowStatus"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSapMipSrcMacAddress"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpMipRowStatus"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpMipSrcMacAddress"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMipGroupV8v0.setStatus("current")

tmnxDot1agCfmMepGroupV8v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 12, 2)
)
tmnxDot1agCfmMepGroupV8v0.setObjects(
    ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepFaultPropagation")
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepGroupV8v0.setStatus("current")

tmnxDot1agCfmMaGroupV9v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 13, 1)
)
tmnxDot1agCfmMaGroupV9v0.setObjects(
    ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMaNetHoldDownTimer")
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaGroupV9v0.setStatus("current")

tmnxDot1agCfmMepGroupV9v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 13, 2)
)
tmnxDot1agCfmMepGroupV9v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepFacilityIfIndex"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepFacilityVlanId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepFacilityType"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepFcltyFaultNotify"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepDescription"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepMcLagInactive"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepGroupV9v0.setStatus("current")

tmnxDot1agCfmGlobalGroupV9v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 13, 3)
)
tmnxDot1agCfmGlobalGroupV9v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMcLagStdbyInactive"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMcLagPropHoldTime"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmGlobalGroupV9v0.setStatus("current")

tmnxDot1agCfmMepSlmGroupV9v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 13, 4)
)
tmnxDot1agCfmMepSlmGroupV9v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSLMInactivityTimer"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmTWTestStatus"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmTWTestId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmTWMacAddress"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmTWPriority"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmTWInterval"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmTWTimeout"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmTWDataSize"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmTWSendCount"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmOWTestStatus"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmOWTestId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmOWMacAddress"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmOWPriority"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmOWInterval"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmOWDataSize"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmOWSendCount"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmTestId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmRemoteMepId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmLastTxSeqF"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmPacketIn"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmPacketLossIn"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmPacketLossOut"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmPacketUnack"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmGroupV9v0.setStatus("current")

tmnxDot1agCfmMepMcastLbmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 13, 6)
)
tmnxDot1agCfmMepMcastLbmGroup.setObjects(
    ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepLbmRxIndex")
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepMcastLbmGroup.setStatus("current")

tmnxDot1agCfmMepSlmTWGroupV10v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 14, 1)
)
tmnxDot1agCfmMepSlmTWGroupV10v0.setObjects(
    ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmTWIntrvlUnits")
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmTWGroupV10v0.setStatus("current")

tmnxDot1agCfmMaGroupV10v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 14, 2)
)
tmnxDot1agCfmMaGroupV10v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMaMepListMacAddress"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMaNetTotalMEPCount"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaGroupV10v0.setStatus("current")

tmnxDot1agCfmMepGroupV10v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 14, 3)
)
tmnxDot1agCfmMepGroupV10v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCcmPaddingSize"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCcmIgnoreTLVs"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepAisLowPrioDef"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepGroupV10v0.setStatus("current")

tmnxDot1agCfmStatsGroupV10v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 14, 4)
)
tmnxDot1agCfmStatsGroupV10v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGlobalPacketRxCount"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGlobalPacketTxCount"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGlobalPacketDropped"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGlobalPacketDiscard"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmCompName"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmCompResourceUsage"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmCompResourceLimit"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmStatsGroupV10v0.setStatus("current")

tmnxDot1agCfmGPGroupV10v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 14, 5)
)
tmnxDot1agCfmGPGroupV10v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGraceTxEnable"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGracePeriod"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepDbGraceRx"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmGPGroupV10v0.setStatus("current")

tmnxDot1agCfmMEPMgmtGroupV11v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 15, 1)
)
tmnxDot1agCfmMEPMgmtGroupV11v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepMgmtRowStatus"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepMgmtType"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepMgmtServiceId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepMgmtIfIndex"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepMgmtPrimaryVid"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepMgmtSdpId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepMgmtVcId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepMgmtFcltyIfIndex"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepMgmtFcltyVlanId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepMgmtDirection"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmPVStackMdIndex"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmPVStackMaIndex"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmPVStackMepId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmPVStackMacAddress"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMEPMgmtGroupV11v0.setStatus("current")

tmnxDot1agCfmMaGroupV11v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 15, 2)
)
tmnxDot1agCfmMaGroupV11v0.setObjects(
    ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMaCompMipLtrPrio")
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaGroupV11v0.setStatus("current")

tmnxDot1agCfmMdGroupV11v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 15, 3)
)
tmnxDot1agCfmMdGroupV11v0.setObjects(
    ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMdCreationOrigin")
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMdGroupV11v0.setStatus("current")

tmnxDot1agCfmMepCSFGroupV11v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 15, 4)
)
tmnxDot1agCfmMepCSFGroupV11v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCsfEnable"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCsfRxMultiplier"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCsfRxState"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCsfRxInterval"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCsfRxCount"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepCSFGroupV11v0.setStatus("current")

tmnxDot1agCfmMaGroupV12v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 16, 1)
)
tmnxDot1agCfmMaGroupV12v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMaNetAutoDiscAdmin"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMaMepListAutoDiscvd"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMaNetIdPermission"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMaGroupV12v0.setStatus("current")

tmnxDot1agCfmStatsGroupV12v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 16, 2)
)
tmnxDot1agCfmStatsGroupV12v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGlobalOpcodeRx"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGlobalOpcodeTx"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGlobalAisTxActive"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGlobalAisTxFail"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmStatsGroupV12v0.setStatus("current")

tmnxDot1agCfmMepGroupV12v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 16, 3)
)
tmnxDot1agCfmMepGroupV12v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepOpcodeRx"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepOpcodeTx"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepEthAisTxFail"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepTxLbmTimeout"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepTxLbmInterval"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepLbmPaddingSize"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepIfSupportEnable"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepGroupV12v0.setStatus("current")

tmnxDot1agCfmScalarsGroupV12v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 16, 4)
)
tmnxDot1agCfmScalarsGroupV12v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSenderIdType"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSenderIdName"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmScalarsGroupV12v0.setStatus("current")


# Notification objects

tmnxDot1agCfmMepLbmTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 52, 0, 1)
)
tmnxDot1agCfmMepLbmTestComplete.setObjects(
    ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLbmDestMacAddress")
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepLbmTestComplete.setStatus(
        "current"
    )

tmnxDot1agCfmMepLtmTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 52, 0, 2)
)
tmnxDot1agCfmMepLtmTestComplete.setObjects(
    ("IEEE8021-CFM-MIB", "dot1agCfmMepTransmitLtmSeqNumber")
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepLtmTestComplete.setStatus(
        "current"
    )

tmnxDot1agCfmMepEthTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 52, 0, 3)
)
tmnxDot1agCfmMepEthTestComplete.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCurrByteCount"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCurrFailedBits"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCurrCrcFailures"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepEthTestComplete.setStatus(
        "current"
    )

tmnxDot1agCfmMepDMTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 52, 0, 4)
)
tmnxDot1agCfmMepDMTestComplete.setObjects(
    ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepDelayTestDelay")
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepDMTestComplete.setStatus(
        "current"
    )

tmnxDot1agCfmMepAisStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 52, 0, 5)
)
tmnxDot1agCfmMepAisStateChanged.setObjects(
    ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepEthRxAis")
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepAisStateChanged.setStatus(
        "current"
    )

tmnxDot1agCfmMipEvaluation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 52, 0, 6)
)
tmnxDot1agCfmMipEvaluation.setObjects(
    ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmNotifySvcId")
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMipEvaluation.setStatus(
        "current"
    )

tmnxDot1agCfmMepSLMTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 52, 0, 7)
)
tmnxDot1agCfmMepSLMTestComplete.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmTestId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmRemoteMepId"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmLastTxSeqF"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmPacketIn"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmPacketLossIn"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmPacketLossOut"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmPacketUnack"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSLMTestComplete.setStatus(
        "current"
    )

tmnxDot1agCfmMepCsfStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 52, 0, 8)
)
tmnxDot1agCfmMepCsfStateChanged.setObjects(
    ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCsfRxState")
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepCsfStateChanged.setStatus(
        "current"
    )


# Notifications groups

tmnxDot1agCfmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 4)
)
tmnxDot1agCfmNotificationGroup.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepLbmTestComplete"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepLtmTestComplete"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmNotificationGroup.setStatus(
        "current"
    )

tmnxY1731CfmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 7)
)
tmnxY1731CfmNotificationGroup.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepEthTestComplete"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepDMTestComplete"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepAisStateChanged"))
)
if mibBuilder.loadTexts:
    tmnxY1731CfmNotificationGroup.setStatus(
        "current"
    )

tmnxDot1agCfmMipNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 9)
)
tmnxDot1agCfmMipNotifyGroup.setObjects(
    ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMipEvaluation")
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMipNotifyGroup.setStatus(
        "current"
    )

tmnxDot1agCfmMepSlmNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 13, 5)
)
tmnxDot1agCfmMepSlmNotifyGroup.setObjects(
    ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSLMTestComplete")
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmMepSlmNotifyGroup.setStatus(
        "current"
    )

tmnxDot1agCfmCSFNotifyGroupV11v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 2, 15, 5)
)
tmnxDot1agCfmCSFNotifyGroupV11v0.setObjects(
    ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCsfStateChanged")
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmCSFNotifyGroupV11v0.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxDot1agCfmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 1, 1)
)
tmnxDot1agCfmCompliance.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpBindStackGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSapStackGroup"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmCompliance.setStatus(
        "obsolete"
    )

tmnxDot1agCfmComplianceV7v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 1, 2)
)
tmnxDot1agCfmComplianceV7v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpBindStackGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSapStackGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmNotificationGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxY1731CfmNotificationGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMipGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMipNotifyGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV7v0"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmComplianceV7v0.setStatus(
        "obsolete"
    )

tmnxDot1agCfmComplianceV8v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 1, 3)
)
tmnxDot1agCfmComplianceV8v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpBindStackGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSapStackGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmNotificationGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxY1731CfmNotificationGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMipNotifyGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMipGroupV8v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV7v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV8v0"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmComplianceV8v0.setStatus(
        "obsolete"
    )

tmnxDot1agCfmComplianceV9v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 1, 4)
)
tmnxDot1agCfmComplianceV9v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMaGroupV9v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpBindStackGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSapStackGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmNotificationGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxY1731CfmNotificationGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMipNotifyGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMipGroupV8v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV7v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV8v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV9v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGlobalGroupV9v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmGroupV9v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmNotifyGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepMcastLbmGroup"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmComplianceV9v0.setStatus(
        "obsolete"
    )

tmnxDot1agCfmComplianceV10v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 1, 5)
)
tmnxDot1agCfmComplianceV10v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGlobalGroupV9v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMaGroupV9v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMaGroupV10v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV7v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV8v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV9v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV10v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepMcastLbmGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmGroupV9v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmNotifyGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmTWGroupV10v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMipGroupV8v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMipNotifyGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmNotificationGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSapStackGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpBindStackGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmStatsGroupV10v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxY1731CfmNotificationGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGPGroupV10v0"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmComplianceV10v0.setStatus(
        "obsolete"
    )

tmnxDot1agCfmComplianceV11v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 1, 6)
)
tmnxDot1agCfmComplianceV11v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGlobalGroupV9v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMaGroupV9v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMaGroupV10v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMaGroupV11v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV7v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV8v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV9v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV10v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCSFGroupV11v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepMcastLbmGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmGroupV9v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmNotifyGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmTWGroupV10v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMipGroupV8v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMipNotifyGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmNotificationGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmCSFNotifyGroupV11v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSapStackGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpBindStackGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmStatsGroupV10v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxY1731CfmNotificationGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGPGroupV10v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMEPMgmtGroupV11v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMdGroupV11v0"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmComplianceV11v0.setStatus(
        "obsolete"
    )

tmnxDot1agCfmComplianceV12v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 52, 1, 7)
)
tmnxDot1agCfmComplianceV12v0.setObjects(
      *(("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGlobalGroupV9v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMaGroupV9v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMaGroupV10v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMaGroupV11v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMaGroupV12v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV7v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV8v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV9v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV10v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepCSFGroupV11v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepGroupV12v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepMcastLbmGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmGroupV9v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmNotifyGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSlmTWGroupV10v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMipGroupV8v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMipNotifyGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmNotificationGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmCSFNotifyGroupV11v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSapStackGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmSdpBindStackGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmStatsGroupV10v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmStatsGroupV12v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxY1731CfmNotificationGroup"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmGPGroupV10v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMEPMgmtGroupV11v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmMdGroupV11v0"),
        ("TIMETRA-IEEE8021-CFM-MIB", "tmnxDot1agCfmScalarsGroupV12v0"))
)
if mibBuilder.loadTexts:
    tmnxDot1agCfmComplianceV12v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-IEEE8021-CFM-MIB",
    **{"Dot1agCfmStatisticOpcodeName": Dot1agCfmStatisticOpcodeName,
       "timetraIEEE8021CfmMIBModule": timetraIEEE8021CfmMIBModule,
       "tmnxDot1agMIBConformance": tmnxDot1agMIBConformance,
       "tmnxDot1agCfmCompliances": tmnxDot1agCfmCompliances,
       "tmnxDot1agCfmCompliance": tmnxDot1agCfmCompliance,
       "tmnxDot1agCfmComplianceV7v0": tmnxDot1agCfmComplianceV7v0,
       "tmnxDot1agCfmComplianceV8v0": tmnxDot1agCfmComplianceV8v0,
       "tmnxDot1agCfmComplianceV9v0": tmnxDot1agCfmComplianceV9v0,
       "tmnxDot1agCfmComplianceV10v0": tmnxDot1agCfmComplianceV10v0,
       "tmnxDot1agCfmComplianceV11v0": tmnxDot1agCfmComplianceV11v0,
       "tmnxDot1agCfmComplianceV12v0": tmnxDot1agCfmComplianceV12v0,
       "tmnxDot1agCfmGroups": tmnxDot1agCfmGroups,
       "tmnxDot1agCfmSdpBindStackGroup": tmnxDot1agCfmSdpBindStackGroup,
       "tmnxDot1agCfmMepGroup": tmnxDot1agCfmMepGroup,
       "tmnxDot1agCfmSapStackGroup": tmnxDot1agCfmSapStackGroup,
       "tmnxDot1agCfmNotificationGroup": tmnxDot1agCfmNotificationGroup,
       "tmnxDot1agCfmMipGroup": tmnxDot1agCfmMipGroup,
       "tmnxDot1agCfmMepGroupV7v0": tmnxDot1agCfmMepGroupV7v0,
       "tmnxY1731CfmNotificationGroup": tmnxY1731CfmNotificationGroup,
       "tmnxDot1agCfmNotifyObjsGroup": tmnxDot1agCfmNotifyObjsGroup,
       "tmnxDot1agCfmMipNotifyGroup": tmnxDot1agCfmMipNotifyGroup,
       "tmnxDot1agCfmV6v0Groups": tmnxDot1agCfmV6v0Groups,
       "tmnxDot1agCfmV7v0Groups": tmnxDot1agCfmV7v0Groups,
       "tmnxDot1agCfmV8v0Groups": tmnxDot1agCfmV8v0Groups,
       "tmnxDot1agCfmMipGroupV8v0": tmnxDot1agCfmMipGroupV8v0,
       "tmnxDot1agCfmMepGroupV8v0": tmnxDot1agCfmMepGroupV8v0,
       "tmnxDot1agCfmV9v0Groups": tmnxDot1agCfmV9v0Groups,
       "tmnxDot1agCfmMaGroupV9v0": tmnxDot1agCfmMaGroupV9v0,
       "tmnxDot1agCfmMepGroupV9v0": tmnxDot1agCfmMepGroupV9v0,
       "tmnxDot1agCfmGlobalGroupV9v0": tmnxDot1agCfmGlobalGroupV9v0,
       "tmnxDot1agCfmMepSlmGroupV9v0": tmnxDot1agCfmMepSlmGroupV9v0,
       "tmnxDot1agCfmMepSlmNotifyGroup": tmnxDot1agCfmMepSlmNotifyGroup,
       "tmnxDot1agCfmMepMcastLbmGroup": tmnxDot1agCfmMepMcastLbmGroup,
       "tmnxDot1agCfmV10v0Groups": tmnxDot1agCfmV10v0Groups,
       "tmnxDot1agCfmMepSlmTWGroupV10v0": tmnxDot1agCfmMepSlmTWGroupV10v0,
       "tmnxDot1agCfmMaGroupV10v0": tmnxDot1agCfmMaGroupV10v0,
       "tmnxDot1agCfmMepGroupV10v0": tmnxDot1agCfmMepGroupV10v0,
       "tmnxDot1agCfmStatsGroupV10v0": tmnxDot1agCfmStatsGroupV10v0,
       "tmnxDot1agCfmGPGroupV10v0": tmnxDot1agCfmGPGroupV10v0,
       "tmnxDot1agCfmV11v0Groups": tmnxDot1agCfmV11v0Groups,
       "tmnxDot1agCfmMEPMgmtGroupV11v0": tmnxDot1agCfmMEPMgmtGroupV11v0,
       "tmnxDot1agCfmMaGroupV11v0": tmnxDot1agCfmMaGroupV11v0,
       "tmnxDot1agCfmMdGroupV11v0": tmnxDot1agCfmMdGroupV11v0,
       "tmnxDot1agCfmMepCSFGroupV11v0": tmnxDot1agCfmMepCSFGroupV11v0,
       "tmnxDot1agCfmCSFNotifyGroupV11v0": tmnxDot1agCfmCSFNotifyGroupV11v0,
       "tmnxDot1agCfmV12v0Groups": tmnxDot1agCfmV12v0Groups,
       "tmnxDot1agCfmMaGroupV12v0": tmnxDot1agCfmMaGroupV12v0,
       "tmnxDot1agCfmStatsGroupV12v0": tmnxDot1agCfmStatsGroupV12v0,
       "tmnxDot1agCfmMepGroupV12v0": tmnxDot1agCfmMepGroupV12v0,
       "tmnxDot1agCfmScalarsGroupV12v0": tmnxDot1agCfmScalarsGroupV12v0,
       "tmnxDot1agMIBObjs": tmnxDot1agMIBObjs,
       "tmnxDot1agCfmStack": tmnxDot1agCfmStack,
       "tmnxDot1agCfmSdpBindStackTable": tmnxDot1agCfmSdpBindStackTable,
       "tmnxDot1agCfmSdpBindStackEntry": tmnxDot1agCfmSdpBindStackEntry,
       "tmnxDot1agCfmSdpBindStackSdpId": tmnxDot1agCfmSdpBindStackSdpId,
       "tmnxDot1agCfmSdpBindStackVcId": tmnxDot1agCfmSdpBindStackVcId,
       "tmnxDot1agCfmSdpBindStackMdLevel": tmnxDot1agCfmSdpBindStackMdLevel,
       "tmnxDot1agCfmSdpBindStackDirection": tmnxDot1agCfmSdpBindStackDirection,
       "tmnxDot1agCfmSdpBindStackMdIndex": tmnxDot1agCfmSdpBindStackMdIndex,
       "tmnxDot1agCfmSdpBindStackMaIndex": tmnxDot1agCfmSdpBindStackMaIndex,
       "tmnxDot1agCfmSdpBindStackMepId": tmnxDot1agCfmSdpBindStackMepId,
       "tmnxDot1agCfmSdpBindStackMacAddress": tmnxDot1agCfmSdpBindStackMacAddress,
       "tmnxDot1agCfmStackTable": tmnxDot1agCfmStackTable,
       "tmnxDot1agCfmStackEntry": tmnxDot1agCfmStackEntry,
       "tmnxDot1agCfmStackifIndex": tmnxDot1agCfmStackifIndex,
       "tmnxDot1agCfmStackVlanIdOrNone": tmnxDot1agCfmStackVlanIdOrNone,
       "tmnxDot1agCfmStackMdLevel": tmnxDot1agCfmStackMdLevel,
       "tmnxDot1agCfmStackDirection": tmnxDot1agCfmStackDirection,
       "tmnxDot1agCfmStackMdIndex": tmnxDot1agCfmStackMdIndex,
       "tmnxDot1agCfmStackMaIndex": tmnxDot1agCfmStackMaIndex,
       "tmnxDot1agCfmStackMepId": tmnxDot1agCfmStackMepId,
       "tmnxDot1agCfmStackMacAddress": tmnxDot1agCfmStackMacAddress,
       "tmnxDot1agCfmStackMPType": tmnxDot1agCfmStackMPType,
       "tmnxDot1agCfmVStackTable": tmnxDot1agCfmVStackTable,
       "tmnxDot1agCfmVStackEntry": tmnxDot1agCfmVStackEntry,
       "tmnxDot1agCfmVStackSvcId": tmnxDot1agCfmVStackSvcId,
       "tmnxDot1agCfmVStackMdLevel": tmnxDot1agCfmVStackMdLevel,
       "tmnxDot1agCfmVStackDirection": tmnxDot1agCfmVStackDirection,
       "tmnxDot1agCfmVStackMdIndex": tmnxDot1agCfmVStackMdIndex,
       "tmnxDot1agCfmVStackMaIndex": tmnxDot1agCfmVStackMaIndex,
       "tmnxDot1agCfmVStackMepId": tmnxDot1agCfmVStackMepId,
       "tmnxDot1agCfmVStackMacAddress": tmnxDot1agCfmVStackMacAddress,
       "tmnxDot1agCfmPVStackTable": tmnxDot1agCfmPVStackTable,
       "tmnxDot1agCfmPVStackEntry": tmnxDot1agCfmPVStackEntry,
       "tmnxDot1agCfmPVStackifIndex": tmnxDot1agCfmPVStackifIndex,
       "tmnxDot1agCfmPVStackVlanIdOrNone": tmnxDot1agCfmPVStackVlanIdOrNone,
       "tmnxDot1agCfmPVStackPriVlanId": tmnxDot1agCfmPVStackPriVlanId,
       "tmnxDot1agCfmPVStackMdLevel": tmnxDot1agCfmPVStackMdLevel,
       "tmnxDot1agCfmPVStackDirection": tmnxDot1agCfmPVStackDirection,
       "tmnxDot1agCfmPVStackMdIndex": tmnxDot1agCfmPVStackMdIndex,
       "tmnxDot1agCfmPVStackMaIndex": tmnxDot1agCfmPVStackMaIndex,
       "tmnxDot1agCfmPVStackMepId": tmnxDot1agCfmPVStackMepId,
       "tmnxDot1agCfmPVStackMacAddress": tmnxDot1agCfmPVStackMacAddress,
       "tmnxDot1agCfmGlobalObjs": tmnxDot1agCfmGlobalObjs,
       "tmnxDot1agCfmMcLagConfigGroup": tmnxDot1agCfmMcLagConfigGroup,
       "tmnxDot1agCfmMcLagStdbyInactive": tmnxDot1agCfmMcLagStdbyInactive,
       "tmnxDot1agCfmMcLagPropHoldTime": tmnxDot1agCfmMcLagPropHoldTime,
       "tmnxDot1agCfmSLMConfigGroup": tmnxDot1agCfmSLMConfigGroup,
       "tmnxDot1agCfmSLMInactivityTimer": tmnxDot1agCfmSLMInactivityTimer,
       "tmnxDot1agCfmStatisticsGroup": tmnxDot1agCfmStatisticsGroup,
       "tmnxDot1agCfmGlobalPacketStats": tmnxDot1agCfmGlobalPacketStats,
       "tmnxDot1agCfmGlobalPacketRxCount": tmnxDot1agCfmGlobalPacketRxCount,
       "tmnxDot1agCfmGlobalPacketTxCount": tmnxDot1agCfmGlobalPacketTxCount,
       "tmnxDot1agCfmGlobalPacketDropped": tmnxDot1agCfmGlobalPacketDropped,
       "tmnxDot1agCfmGlobalPacketDiscard": tmnxDot1agCfmGlobalPacketDiscard,
       "tmnxDot1agCfmGlobalAisTxActive": tmnxDot1agCfmGlobalAisTxActive,
       "tmnxDot1agCfmGlobalAisTxFail": tmnxDot1agCfmGlobalAisTxFail,
       "tmnxDot1agCfmComponentLimitTable": tmnxDot1agCfmComponentLimitTable,
       "tmnxDot1agCfmComponentLimitEntry": tmnxDot1agCfmComponentLimitEntry,
       "tmnxDot1agCfmCompMajorIndex": tmnxDot1agCfmCompMajorIndex,
       "tmnxDot1agCfmCompMinorIndex": tmnxDot1agCfmCompMinorIndex,
       "tmnxDot1agCfmCompName": tmnxDot1agCfmCompName,
       "tmnxDot1agCfmCompResourceUsage": tmnxDot1agCfmCompResourceUsage,
       "tmnxDot1agCfmCompResourceLimit": tmnxDot1agCfmCompResourceLimit,
       "tmnxDot1agCfmGlobalOpcodeTable": tmnxDot1agCfmGlobalOpcodeTable,
       "tmnxDot1agCfmGlobalOpcodeEntry": tmnxDot1agCfmGlobalOpcodeEntry,
       "tmnxDot1agCfmGlobalOpcode": tmnxDot1agCfmGlobalOpcode,
       "tmnxDot1agCfmGlobalOpcodeRx": tmnxDot1agCfmGlobalOpcodeRx,
       "tmnxDot1agCfmGlobalOpcodeTx": tmnxDot1agCfmGlobalOpcodeTx,
       "tmnxDot1agCfmSystemScalarsGroup": tmnxDot1agCfmSystemScalarsGroup,
       "tmnxDot1agCfmGraceTxEnable": tmnxDot1agCfmGraceTxEnable,
       "tmnxDot1agCfmGracePeriod": tmnxDot1agCfmGracePeriod,
       "tmnxDot1agCfmSenderIdType": tmnxDot1agCfmSenderIdType,
       "tmnxDot1agCfmSenderIdName": tmnxDot1agCfmSenderIdName,
       "tmnxDot1agCfmManagementObjects": tmnxDot1agCfmManagementObjects,
       "tmnxDot1agCfmMepMgmtTable": tmnxDot1agCfmMepMgmtTable,
       "tmnxDot1agCfmMepMgmtEntry": tmnxDot1agCfmMepMgmtEntry,
       "tmnxDot1agCfmMepMgmtRowStatus": tmnxDot1agCfmMepMgmtRowStatus,
       "tmnxDot1agCfmMepMgmtType": tmnxDot1agCfmMepMgmtType,
       "tmnxDot1agCfmMepMgmtServiceId": tmnxDot1agCfmMepMgmtServiceId,
       "tmnxDot1agCfmMepMgmtIfIndex": tmnxDot1agCfmMepMgmtIfIndex,
       "tmnxDot1agCfmMepMgmtPrimaryVid": tmnxDot1agCfmMepMgmtPrimaryVid,
       "tmnxDot1agCfmMepMgmtSdpId": tmnxDot1agCfmMepMgmtSdpId,
       "tmnxDot1agCfmMepMgmtVcId": tmnxDot1agCfmMepMgmtVcId,
       "tmnxDot1agCfmMepMgmtFcltyIfIndex": tmnxDot1agCfmMepMgmtFcltyIfIndex,
       "tmnxDot1agCfmMepMgmtFcltyVlanId": tmnxDot1agCfmMepMgmtFcltyVlanId,
       "tmnxDot1agCfmMepMgmtDirection": tmnxDot1agCfmMepMgmtDirection,
       "tmnxDot1agCfmMd": tmnxDot1agCfmMd,
       "tmnxDot1agCfmMdTable": tmnxDot1agCfmMdTable,
       "tmnxDot1agCfmMdEntry": tmnxDot1agCfmMdEntry,
       "tmnxDot1agCfmMdCreationOrigin": tmnxDot1agCfmMdCreationOrigin,
       "tmnxDot1agCfmMa": tmnxDot1agCfmMa,
       "tmnxDot1agCfmMaNetTable": tmnxDot1agCfmMaNetTable,
       "tmnxDot1agCfmMaNetEntry": tmnxDot1agCfmMaNetEntry,
       "tmnxDot1agCfmMaNetHoldDownTimer": tmnxDot1agCfmMaNetHoldDownTimer,
       "tmnxDot1agCfmMaNetTotalMEPCount": tmnxDot1agCfmMaNetTotalMEPCount,
       "tmnxDot1agCfmMaNetAutoDiscAdmin": tmnxDot1agCfmMaNetAutoDiscAdmin,
       "tmnxDot1agCfmMaNetIdPermission": tmnxDot1agCfmMaNetIdPermission,
       "tmnxDot1agCfmMaCompTable": tmnxDot1agCfmMaCompTable,
       "tmnxDot1agCfmMaCompEntry": tmnxDot1agCfmMaCompEntry,
       "tmnxDot1agCfmMaCompMipLtrPrio": tmnxDot1agCfmMaCompMipLtrPrio,
       "tmnxDot1agCfmMaMepListTable": tmnxDot1agCfmMaMepListTable,
       "tmnxDot1agCfmMaMepListEntry": tmnxDot1agCfmMaMepListEntry,
       "tmnxDot1agCfmMaMepListMacAddress": tmnxDot1agCfmMaMepListMacAddress,
       "tmnxDot1agCfmMaMepListAutoDiscvd": tmnxDot1agCfmMaMepListAutoDiscvd,
       "tmnxDot1agCfmMep": tmnxDot1agCfmMep,
       "tmnxDot1agCfmMepTable": tmnxDot1agCfmMepTable,
       "tmnxDot1agCfmMepEntry": tmnxDot1agCfmMepEntry,
       "tmnxDot1agCfmMepSdpId": tmnxDot1agCfmMepSdpId,
       "tmnxDot1agCfmMepVcId": tmnxDot1agCfmMepVcId,
       "tmnxDot1agCfmMepMacAddress": tmnxDot1agCfmMepMacAddress,
       "tmnxDot1agCfmMepAisEnable": tmnxDot1agCfmMepAisEnable,
       "tmnxDot1agCfmMepAisMegLevel": tmnxDot1agCfmMepAisMegLevel,
       "tmnxDot1agCfmMepAisPriority": tmnxDot1agCfmMepAisPriority,
       "tmnxDot1agCfmMepAisInterval": tmnxDot1agCfmMepAisInterval,
       "tmnxDot1agCfmMepEthRxAisInterval": tmnxDot1agCfmMepEthRxAisInterval,
       "tmnxDot1agCfmMepEthRxAis": tmnxDot1agCfmMepEthRxAis,
       "tmnxDot1agCfmMepEthAisTxCount": tmnxDot1agCfmMepEthAisTxCount,
       "tmnxDot1agCfmMepEthTestEnable": tmnxDot1agCfmMepEthTestEnable,
       "tmnxDot1agCfmMepEthTestPattern": tmnxDot1agCfmMepEthTestPattern,
       "tmnxDot1agCfmMepEthTestMacAddr": tmnxDot1agCfmMepEthTestMacAddr,
       "tmnxDot1agCfmMepEthTestDataLen": tmnxDot1agCfmMepEthTestDataLen,
       "tmnxDot1agCfmMepEthTestPriority": tmnxDot1agCfmMepEthTestPriority,
       "tmnxDot1agCfmMepOWDTMacAddress": tmnxDot1agCfmMepOWDTMacAddress,
       "tmnxDot1agCfmMepOWDTPriority": tmnxDot1agCfmMepOWDTPriority,
       "tmnxDot1agCfmMepTWDTMacAddress": tmnxDot1agCfmMepTWDTMacAddress,
       "tmnxDot1agCfmMepTWDTPriority": tmnxDot1agCfmMepTWDTPriority,
       "tmnxDot1agCfmMepSvcId": tmnxDot1agCfmMepSvcId,
       "tmnxDot1agCfmMepControlMep": tmnxDot1agCfmMepControlMep,
       "tmnxDot1agCfmMepEthTestThreshold": tmnxDot1agCfmMepEthTestThreshold,
       "tmnxDot1agCfmMepOWDTThreshold": tmnxDot1agCfmMepOWDTThreshold,
       "tmnxDot1agCfmMepFaultPropagation": tmnxDot1agCfmMepFaultPropagation,
       "tmnxDot1agCfmMepFacilityIfIndex": tmnxDot1agCfmMepFacilityIfIndex,
       "tmnxDot1agCfmMepFacilityVlanId": tmnxDot1agCfmMepFacilityVlanId,
       "tmnxDot1agCfmMepFacilityType": tmnxDot1agCfmMepFacilityType,
       "tmnxDot1agCfmMepFcltyFaultNotify": tmnxDot1agCfmMepFcltyFaultNotify,
       "tmnxDot1agCfmMepDescription": tmnxDot1agCfmMepDescription,
       "tmnxDot1agCfmMepMcLagInactive": tmnxDot1agCfmMepMcLagInactive,
       "tmnxDot1agCfmMepCcmPaddingSize": tmnxDot1agCfmMepCcmPaddingSize,
       "tmnxDot1agCfmMepCcmIgnoreTLVs": tmnxDot1agCfmMepCcmIgnoreTLVs,
       "tmnxDot1agCfmMepCsfEnable": tmnxDot1agCfmMepCsfEnable,
       "tmnxDot1agCfmMepCsfRxMultiplier": tmnxDot1agCfmMepCsfRxMultiplier,
       "tmnxDot1agCfmMepCsfRxState": tmnxDot1agCfmMepCsfRxState,
       "tmnxDot1agCfmMepCsfRxInterval": tmnxDot1agCfmMepCsfRxInterval,
       "tmnxDot1agCfmMepCsfRxCount": tmnxDot1agCfmMepCsfRxCount,
       "tmnxDot1agCfmMepEthAisTxFail": tmnxDot1agCfmMepEthAisTxFail,
       "tmnxDot1agCfmMepTxLbmTimeout": tmnxDot1agCfmMepTxLbmTimeout,
       "tmnxDot1agCfmMepTxLbmInterval": tmnxDot1agCfmMepTxLbmInterval,
       "tmnxDot1agCfmMepLbmPaddingSize": tmnxDot1agCfmMepLbmPaddingSize,
       "tmnxDot1agCfmMepIfSupportEnable": tmnxDot1agCfmMepIfSupportEnable,
       "tmnxDot1agCfmMepAisLowPrioDef": tmnxDot1agCfmMepAisLowPrioDef,
       "tmnxDot1agCfmMepEthTestRsltTable": tmnxDot1agCfmMepEthTestRsltTable,
       "tmnxDot1agCfmMepEthTestRsltEntry": tmnxDot1agCfmMepEthTestRsltEntry,
       "tmnxDot1agCfmMepSrcMacAddress": tmnxDot1agCfmMepSrcMacAddress,
       "tmnxDot1agCfmMepFrameCount": tmnxDot1agCfmMepFrameCount,
       "tmnxDot1agCfmMepByteCount": tmnxDot1agCfmMepByteCount,
       "tmnxDot1agCfmMepFailedBits": tmnxDot1agCfmMepFailedBits,
       "tmnxDot1agCfmMepCrcFailures": tmnxDot1agCfmMepCrcFailures,
       "tmnxDot1agCfmMepCurrByteCount": tmnxDot1agCfmMepCurrByteCount,
       "tmnxDot1agCfmMepCurrFailedBits": tmnxDot1agCfmMepCurrFailedBits,
       "tmnxDot1agCfmMepCurrCrcFailures": tmnxDot1agCfmMepCurrCrcFailures,
       "tmnxDot1agCfmMepDelayRsltTable": tmnxDot1agCfmMepDelayRsltTable,
       "tmnxDot1agCfmMepDelayRsltEntry": tmnxDot1agCfmMepDelayRsltEntry,
       "tmnxDot1agCfmMepDelaySrcMacAddr": tmnxDot1agCfmMepDelaySrcMacAddr,
       "tmnxDot1agCfmMepDelayTestType": tmnxDot1agCfmMepDelayTestType,
       "tmnxDot1agCfmMepDelayTestDelay": tmnxDot1agCfmMepDelayTestDelay,
       "tmnxDot1agCfmMepDelayVariation": tmnxDot1agCfmMepDelayVariation,
       "tmnxDot1agCfmMepSlmTWTestTable": tmnxDot1agCfmMepSlmTWTestTable,
       "tmnxDot1agCfmMepSlmTWTestEntry": tmnxDot1agCfmMepSlmTWTestEntry,
       "tmnxDot1agCfmMepSlmTWTestStatus": tmnxDot1agCfmMepSlmTWTestStatus,
       "tmnxDot1agCfmMepSlmTWTestId": tmnxDot1agCfmMepSlmTWTestId,
       "tmnxDot1agCfmMepSlmTWMacAddress": tmnxDot1agCfmMepSlmTWMacAddress,
       "tmnxDot1agCfmMepSlmTWPriority": tmnxDot1agCfmMepSlmTWPriority,
       "tmnxDot1agCfmMepSlmTWInterval": tmnxDot1agCfmMepSlmTWInterval,
       "tmnxDot1agCfmMepSlmTWTimeout": tmnxDot1agCfmMepSlmTWTimeout,
       "tmnxDot1agCfmMepSlmTWDataSize": tmnxDot1agCfmMepSlmTWDataSize,
       "tmnxDot1agCfmMepSlmTWSendCount": tmnxDot1agCfmMepSlmTWSendCount,
       "tmnxDot1agCfmMepSlmTWIntrvlUnits": tmnxDot1agCfmMepSlmTWIntrvlUnits,
       "tmnxDot1agCfmMepSlmOWTestTable": tmnxDot1agCfmMepSlmOWTestTable,
       "tmnxDot1agCfmMepSlmOWTestEntry": tmnxDot1agCfmMepSlmOWTestEntry,
       "tmnxDot1agCfmMepSlmOWTestStatus": tmnxDot1agCfmMepSlmOWTestStatus,
       "tmnxDot1agCfmMepSlmOWTestId": tmnxDot1agCfmMepSlmOWTestId,
       "tmnxDot1agCfmMepSlmOWMacAddress": tmnxDot1agCfmMepSlmOWMacAddress,
       "tmnxDot1agCfmMepSlmOWPriority": tmnxDot1agCfmMepSlmOWPriority,
       "tmnxDot1agCfmMepSlmOWInterval": tmnxDot1agCfmMepSlmOWInterval,
       "tmnxDot1agCfmMepSlmOWDataSize": tmnxDot1agCfmMepSlmOWDataSize,
       "tmnxDot1agCfmMepSlmOWSendCount": tmnxDot1agCfmMepSlmOWSendCount,
       "tmnxDot1agCfmMepSlmTestRsltTable": tmnxDot1agCfmMepSlmTestRsltTable,
       "tmnxDot1agCfmMepSlmTestRsltEntry": tmnxDot1agCfmMepSlmTestRsltEntry,
       "tmnxDot1agCfmMepSlmTestType": tmnxDot1agCfmMepSlmTestType,
       "tmnxDot1agCfmMepSlmRemoteMacAddr": tmnxDot1agCfmMepSlmRemoteMacAddr,
       "tmnxDot1agCfmMepSlmTestId": tmnxDot1agCfmMepSlmTestId,
       "tmnxDot1agCfmMepSlmRemoteMepId": tmnxDot1agCfmMepSlmRemoteMepId,
       "tmnxDot1agCfmMepSlmLastTxSeqF": tmnxDot1agCfmMepSlmLastTxSeqF,
       "tmnxDot1agCfmMepSlmPacketIn": tmnxDot1agCfmMepSlmPacketIn,
       "tmnxDot1agCfmMepSlmPacketLossIn": tmnxDot1agCfmMepSlmPacketLossIn,
       "tmnxDot1agCfmMepSlmPacketLossOut": tmnxDot1agCfmMepSlmPacketLossOut,
       "tmnxDot1agCfmMepSlmPacketUnack": tmnxDot1agCfmMepSlmPacketUnack,
       "tmnxDot1agCfmMepMcstLbmRsltTable": tmnxDot1agCfmMepMcstLbmRsltTable,
       "tmnxDot1agCfmMepMcstLbmRsltEntry": tmnxDot1agCfmMepMcstLbmRsltEntry,
       "tmnxDot1agCfmMepLbmRemoteMepMac": tmnxDot1agCfmMepLbmRemoteMepMac,
       "tmnxDot1agCfmMepLbmSeqNumber": tmnxDot1agCfmMepLbmSeqNumber,
       "tmnxDot1agCfmMepLbmRxIndex": tmnxDot1agCfmMepLbmRxIndex,
       "tmnxDot1agCfmMepDbTable": tmnxDot1agCfmMepDbTable,
       "tmnxDot1agCfmMepDbEntry": tmnxDot1agCfmMepDbEntry,
       "tmnxDot1agCfmMepDbGraceRx": tmnxDot1agCfmMepDbGraceRx,
       "tmnxDot1agCfmMepOpcodeTable": tmnxDot1agCfmMepOpcodeTable,
       "tmnxDot1agCfmMepOpcodeEntry": tmnxDot1agCfmMepOpcodeEntry,
       "tmnxDot1agCfmMepOpcode": tmnxDot1agCfmMepOpcode,
       "tmnxDot1agCfmMepOpcodeRx": tmnxDot1agCfmMepOpcodeRx,
       "tmnxDot1agCfmMepOpcodeTx": tmnxDot1agCfmMepOpcodeTx,
       "tmnxDot1agCfmMip": tmnxDot1agCfmMip,
       "tmnxDot1agCfmSapMipTable": tmnxDot1agCfmSapMipTable,
       "tmnxDot1agCfmSapMipEntry": tmnxDot1agCfmSapMipEntry,
       "tmnxDot1agCfmSapMipIfIndex": tmnxDot1agCfmSapMipIfIndex,
       "tmnxDot1agCfmSapMipVlanIdOrNone": tmnxDot1agCfmSapMipVlanIdOrNone,
       "tmnxDot1agCfmSapMipRowStatus": tmnxDot1agCfmSapMipRowStatus,
       "tmnxDot1agCfmSapMipSrcMacAddress": tmnxDot1agCfmSapMipSrcMacAddress,
       "tmnxDot1agCfmSapMipPrimaryVlanId": tmnxDot1agCfmSapMipPrimaryVlanId,
       "tmnxDot1agCfmSdpMipTable": tmnxDot1agCfmSdpMipTable,
       "tmnxDot1agCfmSdpMipEntry": tmnxDot1agCfmSdpMipEntry,
       "tmnxDot1agCfmSdpMipSvcId": tmnxDot1agCfmSdpMipSvcId,
       "tmnxDot1agCfmSdpMipSdpId": tmnxDot1agCfmSdpMipSdpId,
       "tmnxDot1agCfmSdpMipVcId": tmnxDot1agCfmSdpMipVcId,
       "tmnxDot1agCfmSdpMipRowStatus": tmnxDot1agCfmSdpMipRowStatus,
       "tmnxDot1agCfmSdpMipSrcMacAddress": tmnxDot1agCfmSdpMipSrcMacAddress,
       "tmnxDot1agCfmNotificationObjs": tmnxDot1agCfmNotificationObjs,
       "tmnxDot1agCfmNotifySvcId": tmnxDot1agCfmNotifySvcId,
       "tmnxDot1agNotificationsPrefix": tmnxDot1agNotificationsPrefix,
       "tmnxDot1agNotifications": tmnxDot1agNotifications,
       "tmnxDot1agCfmMepLbmTestComplete": tmnxDot1agCfmMepLbmTestComplete,
       "tmnxDot1agCfmMepLtmTestComplete": tmnxDot1agCfmMepLtmTestComplete,
       "tmnxDot1agCfmMepEthTestComplete": tmnxDot1agCfmMepEthTestComplete,
       "tmnxDot1agCfmMepDMTestComplete": tmnxDot1agCfmMepDMTestComplete,
       "tmnxDot1agCfmMepAisStateChanged": tmnxDot1agCfmMepAisStateChanged,
       "tmnxDot1agCfmMipEvaluation": tmnxDot1agCfmMipEvaluation,
       "tmnxDot1agCfmMepSLMTestComplete": tmnxDot1agCfmMepSLMTestComplete,
       "tmnxDot1agCfmMepCsfStateChanged": tmnxDot1agCfmMepCsfStateChanged}
)
