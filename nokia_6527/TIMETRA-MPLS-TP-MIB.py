# SNMP MIB module (TIMETRA-MPLS-TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-MPLS-TP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:41:37 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(tmnxChassisNotifyChassisId,
 tmnxChassisNotifyHwIndex,
 tmnxCpmCardEntry,
 tmnxCpmCardOscillatorType) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxChassisNotifyChassisId",
    "tmnxChassisNotifyHwIndex",
    "tmnxCpmCardEntry",
    "tmnxCpmCardOscillatorType")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(vRtrMplsLspIndex,) = mibBuilder.importSymbols(
    "TIMETRA-MPLS-MIB",
    "vRtrMplsLspIndex")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxMplsTpGlobalID,
 TmnxMplsTpNodeID,
 TmnxMplsTpTunnelType,
 TmnxOperState,
 TmnxTunnelID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxMplsTpGlobalID",
    "TmnxMplsTpNodeID",
    "TmnxMplsTpTunnelType",
    "TmnxOperState",
    "TmnxTunnelID")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraMplsTpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 83)
)
if mibBuilder.loadTexts:
    timetraMplsTpMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2012-06-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VRtrMplsTpLspPathMepPduType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



# MIB Managed Objects in the order of their OIDs

_VRtrMplsTpConformance_ObjectIdentity = ObjectIdentity
vRtrMplsTpConformance = _VRtrMplsTpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83)
)
_VRtrMplsTpCompliances_ObjectIdentity = ObjectIdentity
vRtrMplsTpCompliances = _VRtrMplsTpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 1)
)
_VRtrMplsTpGroups_ObjectIdentity = ObjectIdentity
vRtrMplsTpGroups = _VRtrMplsTpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2)
)
_VRtrMplsTpV11v0Groups_ObjectIdentity = ObjectIdentity
vRtrMplsTpV11v0Groups = _VRtrMplsTpV11v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2, 1)
)
_VRtrMplsTpV12v0Groups_ObjectIdentity = ObjectIdentity
vRtrMplsTpV12v0Groups = _VRtrMplsTpV12v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2, 2)
)
_VRtrMplsTpObjs_ObjectIdentity = ObjectIdentity
vRtrMplsTpObjs = _VRtrMplsTpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83)
)
_VRtrMplsTpConfigTimeStamps_ObjectIdentity = ObjectIdentity
vRtrMplsTpConfigTimeStamps = _VRtrMplsTpConfigTimeStamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 1)
)
_VRtrMplsTpSystemTableLastChanged_Type = TimeStamp
_VRtrMplsTpSystemTableLastChanged_Object = MibScalar
vRtrMplsTpSystemTableLastChanged = _VRtrMplsTpSystemTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 1, 1),
    _VRtrMplsTpSystemTableLastChanged_Type()
)
vRtrMplsTpSystemTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpSystemTableLastChanged.setStatus("current")
_VRtrMplsTpOamTemplTblLastChanged_Type = TimeStamp
_VRtrMplsTpOamTemplTblLastChanged_Object = MibScalar
vRtrMplsTpOamTemplTblLastChanged = _VRtrMplsTpOamTemplTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 1, 2),
    _VRtrMplsTpOamTemplTblLastChanged_Type()
)
vRtrMplsTpOamTemplTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpOamTemplTblLastChanged.setStatus("current")
_VRtrMplsTpPtcTemplTblLastChanged_Type = TimeStamp
_VRtrMplsTpPtcTemplTblLastChanged_Object = MibScalar
vRtrMplsTpPtcTemplTblLastChanged = _VRtrMplsTpPtcTemplTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 1, 3),
    _VRtrMplsTpPtcTemplTblLastChanged_Type()
)
vRtrMplsTpPtcTemplTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpPtcTemplTblLastChanged.setStatus("current")
_VRtrMplsTpLspPathTblLastChanged_Type = TimeStamp
_VRtrMplsTpLspPathTblLastChanged_Object = MibScalar
vRtrMplsTpLspPathTblLastChanged = _VRtrMplsTpLspPathTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 1, 5),
    _VRtrMplsTpLspPathTblLastChanged_Type()
)
vRtrMplsTpLspPathTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathTblLastChanged.setStatus("current")
_VRtrMplsTpLspPathMepTblLastChg_Type = TimeStamp
_VRtrMplsTpLspPathMepTblLastChg_Object = MibScalar
vRtrMplsTpLspPathMepTblLastChg = _VRtrMplsTpLspPathMepTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 1, 6),
    _VRtrMplsTpLspPathMepTblLastChg_Type()
)
vRtrMplsTpLspPathMepTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathMepTblLastChg.setStatus("current")
_VRtrMplsTpLsrTblLastChanged_Type = TimeStamp
_VRtrMplsTpLsrTblLastChanged_Object = MibScalar
vRtrMplsTpLsrTblLastChanged = _VRtrMplsTpLsrTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 1, 7),
    _VRtrMplsTpLsrTblLastChanged_Type()
)
vRtrMplsTpLsrTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrTblLastChanged.setStatus("current")
_VRtrMplsTpLsrPathIdTblLastChg_Type = TimeStamp
_VRtrMplsTpLsrPathIdTblLastChg_Object = MibScalar
vRtrMplsTpLsrPathIdTblLastChg = _VRtrMplsTpLsrPathIdTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 1, 8),
    _VRtrMplsTpLsrPathIdTblLastChg_Type()
)
vRtrMplsTpLsrPathIdTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrPathIdTblLastChg.setStatus("current")
_VRtrMplsTpLsrMipCfgTblLastChg_Type = TimeStamp
_VRtrMplsTpLsrMipCfgTblLastChg_Object = MibScalar
vRtrMplsTpLsrMipCfgTblLastChg = _VRtrMplsTpLsrMipCfgTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 1, 9),
    _VRtrMplsTpLsrMipCfgTblLastChg_Type()
)
vRtrMplsTpLsrMipCfgTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrMipCfgTblLastChg.setStatus("current")
_VRtrMplsTpIfTblLastChanged_Type = TimeStamp
_VRtrMplsTpIfTblLastChanged_Object = MibScalar
vRtrMplsTpIfTblLastChanged = _VRtrMplsTpIfTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 1, 10),
    _VRtrMplsTpIfTblLastChanged_Type()
)
vRtrMplsTpIfTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpIfTblLastChanged.setStatus("current")
_VRtrMplsTpConfigurations_ObjectIdentity = ObjectIdentity
vRtrMplsTpConfigurations = _VRtrMplsTpConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2)
)
_VRtrMplsTpSystemIdentifiers_ObjectIdentity = ObjectIdentity
vRtrMplsTpSystemIdentifiers = _VRtrMplsTpSystemIdentifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 1)
)
_VRtrMplsTpSystemTable_Object = MibTable
vRtrMplsTpSystemTable = _VRtrMplsTpSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 1, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsTpSystemTable.setStatus("current")
_VRtrMplsTpSystemEntry_Object = MibTableRow
vRtrMplsTpSystemEntry = _VRtrMplsTpSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 1, 1, 1)
)
vRtrMplsTpSystemEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrMplsTpSystemEntry.setStatus("current")
_VRtrMplsTpRowStatus_Type = RowStatus
_VRtrMplsTpRowStatus_Object = MibTableColumn
vRtrMplsTpRowStatus = _VRtrMplsTpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 1, 1, 1, 1),
    _VRtrMplsTpRowStatus_Type()
)
vRtrMplsTpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpRowStatus.setStatus("current")


class _VRtrMplsTpGlobalId_Type(TmnxMplsTpGlobalID):
    """Custom type vRtrMplsTpGlobalId based on TmnxMplsTpGlobalID"""
    defaultValue = 0


_VRtrMplsTpGlobalId_Type.__name__ = "TmnxMplsTpGlobalID"
_VRtrMplsTpGlobalId_Object = MibTableColumn
vRtrMplsTpGlobalId = _VRtrMplsTpGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 1, 1, 1, 2),
    _VRtrMplsTpGlobalId_Type()
)
vRtrMplsTpGlobalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpGlobalId.setStatus("current")


class _VRtrMplsTpNodeId_Type(TmnxMplsTpNodeID):
    """Custom type vRtrMplsTpNodeId based on TmnxMplsTpNodeID"""
    defaultValue = 0


_VRtrMplsTpNodeId_Type.__name__ = "TmnxMplsTpNodeID"
_VRtrMplsTpNodeId_Object = MibTableColumn
vRtrMplsTpNodeId = _VRtrMplsTpNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 1, 1, 1, 3),
    _VRtrMplsTpNodeId_Type()
)
vRtrMplsTpNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpNodeId.setStatus("current")


class _VRtrMplsTpTunnelIdMin_Type(Unsigned32):
    """Custom type vRtrMplsTpTunnelIdMin based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 61440),
    )


_VRtrMplsTpTunnelIdMin_Type.__name__ = "Unsigned32"
_VRtrMplsTpTunnelIdMin_Object = MibTableColumn
vRtrMplsTpTunnelIdMin = _VRtrMplsTpTunnelIdMin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 1, 1, 1, 4),
    _VRtrMplsTpTunnelIdMin_Type()
)
vRtrMplsTpTunnelIdMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelIdMin.setStatus("current")


class _VRtrMplsTpTunnelIdMax_Type(Unsigned32):
    """Custom type vRtrMplsTpTunnelIdMax based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 61440),
    )


_VRtrMplsTpTunnelIdMax_Type.__name__ = "Unsigned32"
_VRtrMplsTpTunnelIdMax_Object = MibTableColumn
vRtrMplsTpTunnelIdMax = _VRtrMplsTpTunnelIdMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 1, 1, 1, 5),
    _VRtrMplsTpTunnelIdMax_Type()
)
vRtrMplsTpTunnelIdMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelIdMax.setStatus("current")


class _VRtrMplsTpAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsTpAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsTpAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsTpAdminState_Object = MibTableColumn
vRtrMplsTpAdminState = _VRtrMplsTpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 1, 1, 1, 6),
    _VRtrMplsTpAdminState_Type()
)
vRtrMplsTpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpAdminState.setStatus("current")


class _VRtrMplsTpInheritance_Type(Bits):
    """Custom type vRtrMplsTpInheritance based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("vRtrMplsTpNodeId", 0)
    )

_VRtrMplsTpInheritance_Type.__name__ = "Bits"
_VRtrMplsTpInheritance_Object = MibTableColumn
vRtrMplsTpInheritance = _VRtrMplsTpInheritance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 1, 1, 1, 7),
    _VRtrMplsTpInheritance_Type()
)
vRtrMplsTpInheritance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpInheritance.setStatus("current")
_VRtrMplsTpTemplateObjects_ObjectIdentity = ObjectIdentity
vRtrMplsTpTemplateObjects = _VRtrMplsTpTemplateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2)
)
_VRtrMplsTpOamTemplateCfgTable_Object = MibTable
vRtrMplsTpOamTemplateCfgTable = _VRtrMplsTpOamTemplateCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsTpOamTemplateCfgTable.setStatus("current")
_VRtrMplsTpOamTemplateCfgEntry_Object = MibTableRow
vRtrMplsTpOamTemplateCfgEntry = _VRtrMplsTpOamTemplateCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 1, 1)
)
vRtrMplsTpOamTemplateCfgEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpOamTmplName"),
)
if mibBuilder.loadTexts:
    vRtrMplsTpOamTemplateCfgEntry.setStatus("current")
_VRtrMplsTpOamTmplName_Type = TNamedItem
_VRtrMplsTpOamTmplName_Object = MibTableColumn
vRtrMplsTpOamTmplName = _VRtrMplsTpOamTmplName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 1, 1, 1),
    _VRtrMplsTpOamTmplName_Type()
)
vRtrMplsTpOamTmplName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpOamTmplName.setStatus("current")
_VRtrMplsTpOamTmplRowStatus_Type = RowStatus
_VRtrMplsTpOamTmplRowStatus_Object = MibTableColumn
vRtrMplsTpOamTmplRowStatus = _VRtrMplsTpOamTmplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 1, 1, 2),
    _VRtrMplsTpOamTmplRowStatus_Type()
)
vRtrMplsTpOamTmplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpOamTmplRowStatus.setStatus("current")
_VRtrMplsTpOamTmplLastChangedTime_Type = TimeStamp
_VRtrMplsTpOamTmplLastChangedTime_Object = MibTableColumn
vRtrMplsTpOamTmplLastChangedTime = _VRtrMplsTpOamTmplLastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 1, 1, 3),
    _VRtrMplsTpOamTmplLastChangedTime_Type()
)
vRtrMplsTpOamTmplLastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpOamTmplLastChangedTime.setStatus("current")
_VRtrMplsTpOamTmplBfdTemplateName_Type = TNamedItemOrEmpty
_VRtrMplsTpOamTmplBfdTemplateName_Object = MibTableColumn
vRtrMplsTpOamTmplBfdTemplateName = _VRtrMplsTpOamTmplBfdTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 1, 1, 4),
    _VRtrMplsTpOamTmplBfdTemplateName_Type()
)
vRtrMplsTpOamTmplBfdTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpOamTmplBfdTemplateName.setStatus("current")


class _VRtrMplsTpOamTmplHoldTimeDown_Type(Unsigned32):
    """Custom type vRtrMplsTpOamTmplHoldTimeDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VRtrMplsTpOamTmplHoldTimeDown_Type.__name__ = "Unsigned32"
_VRtrMplsTpOamTmplHoldTimeDown_Object = MibTableColumn
vRtrMplsTpOamTmplHoldTimeDown = _VRtrMplsTpOamTmplHoldTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 1, 1, 5),
    _VRtrMplsTpOamTmplHoldTimeDown_Type()
)
vRtrMplsTpOamTmplHoldTimeDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpOamTmplHoldTimeDown.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsTpOamTmplHoldTimeDown.setUnits("centiseconds")


class _VRtrMplsTpOamTmplHoldTimeUp_Type(Unsigned32):
    """Custom type vRtrMplsTpOamTmplHoldTimeUp based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_VRtrMplsTpOamTmplHoldTimeUp_Type.__name__ = "Unsigned32"
_VRtrMplsTpOamTmplHoldTimeUp_Object = MibTableColumn
vRtrMplsTpOamTmplHoldTimeUp = _VRtrMplsTpOamTmplHoldTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 1, 1, 6),
    _VRtrMplsTpOamTmplHoldTimeUp_Type()
)
vRtrMplsTpOamTmplHoldTimeUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpOamTmplHoldTimeUp.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsTpOamTmplHoldTimeUp.setUnits("deciseconds")
_VRtrMplsTpPtcTemplateCfgTable_Object = MibTable
vRtrMplsTpPtcTemplateCfgTable = _VRtrMplsTpPtcTemplateCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 2)
)
if mibBuilder.loadTexts:
    vRtrMplsTpPtcTemplateCfgTable.setStatus("current")
_VRtrMplsTpPtcTemplateCfgEntry_Object = MibTableRow
vRtrMplsTpPtcTemplateCfgEntry = _VRtrMplsTpPtcTemplateCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 2, 1)
)
vRtrMplsTpPtcTemplateCfgEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpPtcTmplName"),
)
if mibBuilder.loadTexts:
    vRtrMplsTpPtcTemplateCfgEntry.setStatus("current")
_VRtrMplsTpPtcTmplName_Type = TNamedItem
_VRtrMplsTpPtcTmplName_Object = MibTableColumn
vRtrMplsTpPtcTmplName = _VRtrMplsTpPtcTmplName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 2, 1, 1),
    _VRtrMplsTpPtcTmplName_Type()
)
vRtrMplsTpPtcTmplName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpPtcTmplName.setStatus("current")
_VRtrMplsTpPtcTmplRowStatus_Type = RowStatus
_VRtrMplsTpPtcTmplRowStatus_Object = MibTableColumn
vRtrMplsTpPtcTmplRowStatus = _VRtrMplsTpPtcTmplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 2, 1, 2),
    _VRtrMplsTpPtcTmplRowStatus_Type()
)
vRtrMplsTpPtcTmplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpPtcTmplRowStatus.setStatus("current")
_VRtrMplsTpPtcTmplLastChangedTime_Type = TimeStamp
_VRtrMplsTpPtcTmplLastChangedTime_Object = MibTableColumn
vRtrMplsTpPtcTmplLastChangedTime = _VRtrMplsTpPtcTmplLastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 2, 1, 3),
    _VRtrMplsTpPtcTmplLastChangedTime_Type()
)
vRtrMplsTpPtcTmplLastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpPtcTmplLastChangedTime.setStatus("current")


class _VRtrMplsTpPtcTmplProtectionMode_Type(Integer32):
    """Custom type vRtrMplsTpPtcTmplProtectionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("one2one", 1)
    )


_VRtrMplsTpPtcTmplProtectionMode_Type.__name__ = "Integer32"
_VRtrMplsTpPtcTmplProtectionMode_Object = MibTableColumn
vRtrMplsTpPtcTmplProtectionMode = _VRtrMplsTpPtcTmplProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 2, 1, 4),
    _VRtrMplsTpPtcTmplProtectionMode_Type()
)
vRtrMplsTpPtcTmplProtectionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpPtcTmplProtectionMode.setStatus("current")


class _VRtrMplsTpPtcTmplProtectionDir_Type(Integer32):
    """Custom type vRtrMplsTpPtcTmplProtectionDir based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("bidirectional", 2)
    )


_VRtrMplsTpPtcTmplProtectionDir_Type.__name__ = "Integer32"
_VRtrMplsTpPtcTmplProtectionDir_Object = MibTableColumn
vRtrMplsTpPtcTmplProtectionDir = _VRtrMplsTpPtcTmplProtectionDir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 2, 1, 5),
    _VRtrMplsTpPtcTmplProtectionDir_Type()
)
vRtrMplsTpPtcTmplProtectionDir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpPtcTmplProtectionDir.setStatus("current")


class _VRtrMplsTpPtcTmplRevertive_Type(Integer32):
    """Custom type vRtrMplsTpPtcTmplRevertive based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertive", 1),
          ("revertive", 2))
    )


_VRtrMplsTpPtcTmplRevertive_Type.__name__ = "Integer32"
_VRtrMplsTpPtcTmplRevertive_Object = MibTableColumn
vRtrMplsTpPtcTmplRevertive = _VRtrMplsTpPtcTmplRevertive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 2, 1, 6),
    _VRtrMplsTpPtcTmplRevertive_Type()
)
vRtrMplsTpPtcTmplRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpPtcTmplRevertive.setStatus("current")


class _VRtrMplsTpPtcTmplWaitToRestore_Type(Unsigned32):
    """Custom type vRtrMplsTpPtcTmplWaitToRestore based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_VRtrMplsTpPtcTmplWaitToRestore_Type.__name__ = "Unsigned32"
_VRtrMplsTpPtcTmplWaitToRestore_Object = MibTableColumn
vRtrMplsTpPtcTmplWaitToRestore = _VRtrMplsTpPtcTmplWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 2, 1, 7),
    _VRtrMplsTpPtcTmplWaitToRestore_Type()
)
vRtrMplsTpPtcTmplWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpPtcTmplWaitToRestore.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsTpPtcTmplWaitToRestore.setUnits("seconds")


class _VRtrMplsTpPtcTmplRapidPscTimer_Type(Unsigned32):
    """Custom type vRtrMplsTpPtcTmplRapidPscTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(1000, 1000),
    )


_VRtrMplsTpPtcTmplRapidPscTimer_Type.__name__ = "Unsigned32"
_VRtrMplsTpPtcTmplRapidPscTimer_Object = MibTableColumn
vRtrMplsTpPtcTmplRapidPscTimer = _VRtrMplsTpPtcTmplRapidPscTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 2, 1, 8),
    _VRtrMplsTpPtcTmplRapidPscTimer_Type()
)
vRtrMplsTpPtcTmplRapidPscTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpPtcTmplRapidPscTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsTpPtcTmplRapidPscTimer.setUnits("milliseconds")


class _VRtrMplsTpPtcTmplSlowPscTimer_Type(Unsigned32):
    """Custom type vRtrMplsTpPtcTmplSlowPscTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_VRtrMplsTpPtcTmplSlowPscTimer_Type.__name__ = "Unsigned32"
_VRtrMplsTpPtcTmplSlowPscTimer_Object = MibTableColumn
vRtrMplsTpPtcTmplSlowPscTimer = _VRtrMplsTpPtcTmplSlowPscTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 2, 2, 1, 9),
    _VRtrMplsTpPtcTmplSlowPscTimer_Type()
)
vRtrMplsTpPtcTmplSlowPscTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpPtcTmplSlowPscTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsTpPtcTmplSlowPscTimer.setUnits("seconds")
_VRtrMplsTpLspObjects_ObjectIdentity = ObjectIdentity
vRtrMplsTpLspObjects = _VRtrMplsTpLspObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3)
)
_VRtrMplsTpLspPathTable_Object = MibTable
vRtrMplsTpLspPathTable = _VRtrMplsTpLspPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2)
)
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathTable.setStatus("current")
_VRtrMplsTpLspPathEntry_Object = MibTableRow
vRtrMplsTpLspPathEntry = _VRtrMplsTpLspPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2, 1)
)
vRtrMplsTpLspPathEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathEntry.setStatus("current")


class _VRtrMplsTpLspPathIndex_Type(Integer32):
    """Custom type vRtrMplsTpLspPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("working", 1),
          ("protecting", 2))
    )


_VRtrMplsTpLspPathIndex_Type.__name__ = "Integer32"
_VRtrMplsTpLspPathIndex_Object = MibTableColumn
vRtrMplsTpLspPathIndex = _VRtrMplsTpLspPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2, 1, 1),
    _VRtrMplsTpLspPathIndex_Type()
)
vRtrMplsTpLspPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathIndex.setStatus("current")
_VRtrMplsTpLspPathRowStatus_Type = RowStatus
_VRtrMplsTpLspPathRowStatus_Object = MibTableColumn
vRtrMplsTpLspPathRowStatus = _VRtrMplsTpLspPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2, 1, 2),
    _VRtrMplsTpLspPathRowStatus_Type()
)
vRtrMplsTpLspPathRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathRowStatus.setStatus("current")
_VRtrMplsTpLspPathLastChangedTime_Type = TimeStamp
_VRtrMplsTpLspPathLastChangedTime_Object = MibTableColumn
vRtrMplsTpLspPathLastChangedTime = _VRtrMplsTpLspPathLastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2, 1, 3),
    _VRtrMplsTpLspPathLastChangedTime_Type()
)
vRtrMplsTpLspPathLastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathLastChangedTime.setStatus("current")


class _VRtrMplsTpLspPathAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsTpLspPathAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsTpLspPathAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsTpLspPathAdminState_Object = MibTableColumn
vRtrMplsTpLspPathAdminState = _VRtrMplsTpLspPathAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2, 1, 4),
    _VRtrMplsTpLspPathAdminState_Type()
)
vRtrMplsTpLspPathAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathAdminState.setStatus("current")
_VRtrMplsTpLspPathOperState_Type = TmnxOperState
_VRtrMplsTpLspPathOperState_Object = MibTableColumn
vRtrMplsTpLspPathOperState = _VRtrMplsTpLspPathOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2, 1, 5),
    _VRtrMplsTpLspPathOperState_Type()
)
vRtrMplsTpLspPathOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathOperState.setStatus("current")


class _VRtrMplsTpLspPathReasonDownFlags_Type(Bits):
    """Custom type vRtrMplsTpLspPathReasonDownFlags based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ccFault", 1),
          ("cvFault", 2),
          ("ifDn", 3),
          ("portDn", 4),
          ("parentAdminDn", 5),
          ("mepAdminDn", 6),
          ("unsupportedPort", 7),
          ("ifNhAddrInconsistent", 8),
          ("ptcTmplMsng", 9),
          ("ccDnHold", 10),
          ("ccUpHold", 11),
          ("bfdNoRsrc", 12))
    )

_VRtrMplsTpLspPathReasonDownFlags_Type.__name__ = "Bits"
_VRtrMplsTpLspPathReasonDownFlags_Object = MibTableColumn
vRtrMplsTpLspPathReasonDownFlags = _VRtrMplsTpLspPathReasonDownFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2, 1, 6),
    _VRtrMplsTpLspPathReasonDownFlags_Type()
)
vRtrMplsTpLspPathReasonDownFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathReasonDownFlags.setStatus("current")


class _VRtrMplsTpLspPathLspNumber_Type(Unsigned32):
    """Custom type vRtrMplsTpLspPathLspNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrMplsTpLspPathLspNumber_Type.__name__ = "Unsigned32"
_VRtrMplsTpLspPathLspNumber_Object = MibTableColumn
vRtrMplsTpLspPathLspNumber = _VRtrMplsTpLspPathLspNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2, 1, 7),
    _VRtrMplsTpLspPathLspNumber_Type()
)
vRtrMplsTpLspPathLspNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathLspNumber.setStatus("current")


class _VRtrMplsTpLspPathInLabel_Type(Unsigned32):
    """Custom type vRtrMplsTpLspPathInLabel based on Unsigned32"""
    defaultValue = 0


_VRtrMplsTpLspPathInLabel_Type.__name__ = "Unsigned32"
_VRtrMplsTpLspPathInLabel_Object = MibTableColumn
vRtrMplsTpLspPathInLabel = _VRtrMplsTpLspPathInLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2, 1, 8),
    _VRtrMplsTpLspPathInLabel_Type()
)
vRtrMplsTpLspPathInLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathInLabel.setStatus("current")


class _VRtrMplsTpLspPathOutLabel_Type(Unsigned32):
    """Custom type vRtrMplsTpLspPathOutLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1048575),
    )


_VRtrMplsTpLspPathOutLabel_Type.__name__ = "Unsigned32"
_VRtrMplsTpLspPathOutLabel_Object = MibTableColumn
vRtrMplsTpLspPathOutLabel = _VRtrMplsTpLspPathOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2, 1, 9),
    _VRtrMplsTpLspPathOutLabel_Type()
)
vRtrMplsTpLspPathOutLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathOutLabel.setStatus("current")


class _VRtrMplsTpLspPathOutLink_Type(InterfaceIndexOrZero):
    """Custom type vRtrMplsTpLspPathOutLink based on InterfaceIndexOrZero"""
    defaultValue = 0


_VRtrMplsTpLspPathOutLink_Type.__name__ = "InterfaceIndexOrZero"
_VRtrMplsTpLspPathOutLink_Object = MibTableColumn
vRtrMplsTpLspPathOutLink = _VRtrMplsTpLspPathOutLink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2, 1, 10),
    _VRtrMplsTpLspPathOutLink_Type()
)
vRtrMplsTpLspPathOutLink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathOutLink.setStatus("current")


class _VRtrMplsTpLspPathNextHopAddrType_Type(InetAddressType):
    """Custom type vRtrMplsTpLspPathNextHopAddrType based on InetAddressType"""
    defaultValue = 0


_VRtrMplsTpLspPathNextHopAddrType_Type.__name__ = "InetAddressType"
_VRtrMplsTpLspPathNextHopAddrType_Object = MibTableColumn
vRtrMplsTpLspPathNextHopAddrType = _VRtrMplsTpLspPathNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2, 1, 11),
    _VRtrMplsTpLspPathNextHopAddrType_Type()
)
vRtrMplsTpLspPathNextHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathNextHopAddrType.setStatus("current")


class _VRtrMplsTpLspPathNextHopAddress_Type(InetAddress):
    """Custom type vRtrMplsTpLspPathNextHopAddress based on InetAddress"""
    defaultValue = OctetString("")

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsTpLspPathNextHopAddress_Type.__name__ = "InetAddress"
_VRtrMplsTpLspPathNextHopAddress_Object = MibTableColumn
vRtrMplsTpLspPathNextHopAddress = _VRtrMplsTpLspPathNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2, 1, 12),
    _VRtrMplsTpLspPathNextHopAddress_Type()
)
vRtrMplsTpLspPathNextHopAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathNextHopAddress.setStatus("current")


class _VRtrMplsTpLspPathState_Type(Integer32):
    """Custom type vRtrMplsTpLspPathState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("active", 2),
          ("inactive", 3))
    )


_VRtrMplsTpLspPathState_Type.__name__ = "Integer32"
_VRtrMplsTpLspPathState_Object = MibTableColumn
vRtrMplsTpLspPathState = _VRtrMplsTpLspPathState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2, 1, 13),
    _VRtrMplsTpLspPathState_Type()
)
vRtrMplsTpLspPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathState.setStatus("current")
_VRtrMplsTpLspPathTimeUp_Type = TimeInterval
_VRtrMplsTpLspPathTimeUp_Object = MibTableColumn
vRtrMplsTpLspPathTimeUp = _VRtrMplsTpLspPathTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2, 1, 14),
    _VRtrMplsTpLspPathTimeUp_Type()
)
vRtrMplsTpLspPathTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathTimeUp.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathTimeUp.setUnits("centiseconds")
_VRtrMplsTpLspPathTimeDown_Type = TimeInterval
_VRtrMplsTpLspPathTimeDown_Object = MibTableColumn
vRtrMplsTpLspPathTimeDown = _VRtrMplsTpLspPathTimeDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2, 1, 15),
    _VRtrMplsTpLspPathTimeDown_Type()
)
vRtrMplsTpLspPathTimeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathTimeDown.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathTimeDown.setUnits("centiseconds")
_VRtrMplsTpLspPathActiveTimeUp_Type = TimeInterval
_VRtrMplsTpLspPathActiveTimeUp_Object = MibTableColumn
vRtrMplsTpLspPathActiveTimeUp = _VRtrMplsTpLspPathActiveTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 2, 1, 16),
    _VRtrMplsTpLspPathActiveTimeUp_Type()
)
vRtrMplsTpLspPathActiveTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathActiveTimeUp.setStatus("current")
_VRtrMplsTpLspPathMepTable_Object = MibTable
vRtrMplsTpLspPathMepTable = _VRtrMplsTpLspPathMepTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 3)
)
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathMepTable.setStatus("current")
_VRtrMplsTpLspPathMepEntry_Object = MibTableRow
vRtrMplsTpLspPathMepEntry = _VRtrMplsTpLspPathMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 3, 1)
)
vRtrMplsTpLspPathMepEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathMepEntry.setStatus("current")
_VRtrMplsTpLspPathMepLastChgTime_Type = TimeStamp
_VRtrMplsTpLspPathMepLastChgTime_Object = MibTableColumn
vRtrMplsTpLspPathMepLastChgTime = _VRtrMplsTpLspPathMepLastChgTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 3, 1, 1),
    _VRtrMplsTpLspPathMepLastChgTime_Type()
)
vRtrMplsTpLspPathMepLastChgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathMepLastChgTime.setStatus("current")
_VRtrMplsTpLspPathMepRowStatus_Type = RowStatus
_VRtrMplsTpLspPathMepRowStatus_Object = MibTableColumn
vRtrMplsTpLspPathMepRowStatus = _VRtrMplsTpLspPathMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 3, 1, 2),
    _VRtrMplsTpLspPathMepRowStatus_Type()
)
vRtrMplsTpLspPathMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathMepRowStatus.setStatus("current")


class _VRtrMplsTpLspPathMepAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsTpLspPathMepAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsTpLspPathMepAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsTpLspPathMepAdminState_Object = MibTableColumn
vRtrMplsTpLspPathMepAdminState = _VRtrMplsTpLspPathMepAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 3, 1, 3),
    _VRtrMplsTpLspPathMepAdminState_Type()
)
vRtrMplsTpLspPathMepAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathMepAdminState.setStatus("current")


class _VRtrMplsTpLspPathMepProtectTmpl_Type(TNamedItemOrEmpty):
    """Custom type vRtrMplsTpLspPathMepProtectTmpl based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_VRtrMplsTpLspPathMepProtectTmpl_Type.__name__ = "TNamedItemOrEmpty"
_VRtrMplsTpLspPathMepProtectTmpl_Object = MibTableColumn
vRtrMplsTpLspPathMepProtectTmpl = _VRtrMplsTpLspPathMepProtectTmpl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 3, 1, 4),
    _VRtrMplsTpLspPathMepProtectTmpl_Type()
)
vRtrMplsTpLspPathMepProtectTmpl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathMepProtectTmpl.setStatus("current")


class _VRtrMplsTpLspPathMepOamTmpl_Type(TNamedItemOrEmpty):
    """Custom type vRtrMplsTpLspPathMepOamTmpl based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_VRtrMplsTpLspPathMepOamTmpl_Type.__name__ = "TNamedItemOrEmpty"
_VRtrMplsTpLspPathMepOamTmpl_Object = MibTableColumn
vRtrMplsTpLspPathMepOamTmpl = _VRtrMplsTpLspPathMepOamTmpl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 3, 1, 5),
    _VRtrMplsTpLspPathMepOamTmpl_Type()
)
vRtrMplsTpLspPathMepOamTmpl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathMepOamTmpl.setStatus("current")


class _VRtrMplsTpLspPathMepBfdEnabled_Type(Integer32):
    """Custom type vRtrMplsTpLspPathMepBfdEnabled based on Integer32"""
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
          ("cc", 1),
          ("ccCv", 2))
    )


_VRtrMplsTpLspPathMepBfdEnabled_Type.__name__ = "Integer32"
_VRtrMplsTpLspPathMepBfdEnabled_Object = MibTableColumn
vRtrMplsTpLspPathMepBfdEnabled = _VRtrMplsTpLspPathMepBfdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 3, 1, 6),
    _VRtrMplsTpLspPathMepBfdEnabled_Type()
)
vRtrMplsTpLspPathMepBfdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathMepBfdEnabled.setStatus("current")
_VRtrMplsTpLspPathMepBfdOperState_Type = TmnxOperState
_VRtrMplsTpLspPathMepBfdOperState_Object = MibTableColumn
vRtrMplsTpLspPathMepBfdOperState = _VRtrMplsTpLspPathMepBfdOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 3, 1, 7),
    _VRtrMplsTpLspPathMepBfdOperState_Type()
)
vRtrMplsTpLspPathMepBfdOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathMepBfdOperState.setStatus("current")


class _VRtrMplsTpLspPathMepDSInIfNum_Type(Unsigned32):
    """Custom type vRtrMplsTpLspPathMepDSInIfNum based on Unsigned32"""
    defaultValue = 0


_VRtrMplsTpLspPathMepDSInIfNum_Type.__name__ = "Unsigned32"
_VRtrMplsTpLspPathMepDSInIfNum_Object = MibTableColumn
vRtrMplsTpLspPathMepDSInIfNum = _VRtrMplsTpLspPathMepDSInIfNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 3, 1, 8),
    _VRtrMplsTpLspPathMepDSInIfNum_Type()
)
vRtrMplsTpLspPathMepDSInIfNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathMepDSInIfNum.setStatus("current")


class _VRtrMplsTpLspPathMepDSOutIfNum_Type(Unsigned32):
    """Custom type vRtrMplsTpLspPathMepDSOutIfNum based on Unsigned32"""
    defaultValue = 0


_VRtrMplsTpLspPathMepDSOutIfNum_Type.__name__ = "Unsigned32"
_VRtrMplsTpLspPathMepDSOutIfNum_Object = MibTableColumn
vRtrMplsTpLspPathMepDSOutIfNum = _VRtrMplsTpLspPathMepDSOutIfNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 3, 1, 9),
    _VRtrMplsTpLspPathMepDSOutIfNum_Type()
)
vRtrMplsTpLspPathMepDSOutIfNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathMepDSOutIfNum.setStatus("current")
_VRtrMplsTpLspPtPathMepStatTable_Object = MibTable
vRtrMplsTpLspPtPathMepStatTable = _VRtrMplsTpLspPtPathMepStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 4)
)
if mibBuilder.loadTexts:
    vRtrMplsTpLspPtPathMepStatTable.setStatus("current")
_VRtrMplsTpLspPtPathMepStatEntry_Object = MibTableRow
vRtrMplsTpLspPtPathMepStatEntry = _VRtrMplsTpLspPtPathMepStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 4, 1)
)
vRtrMplsTpLspPtPathMepStatEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsTpLspPtPathMepStatEntry.setStatus("current")
_VRtrMplsTpLspPtPathMepRxPdu_Type = VRtrMplsTpLspPathMepPduType
_VRtrMplsTpLspPtPathMepRxPdu_Object = MibTableColumn
vRtrMplsTpLspPtPathMepRxPdu = _VRtrMplsTpLspPtPathMepRxPdu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 4, 1, 1),
    _VRtrMplsTpLspPtPathMepRxPdu_Type()
)
vRtrMplsTpLspPtPathMepRxPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPtPathMepRxPdu.setStatus("current")
_VRtrMplsTpLspPtPathMepTxPdu_Type = VRtrMplsTpLspPathMepPduType
_VRtrMplsTpLspPtPathMepTxPdu_Object = MibTableColumn
vRtrMplsTpLspPtPathMepTxPdu = _VRtrMplsTpLspPtPathMepTxPdu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 4, 1, 2),
    _VRtrMplsTpLspPtPathMepTxPdu_Type()
)
vRtrMplsTpLspPtPathMepTxPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPtPathMepTxPdu.setStatus("current")


class _VRtrMplsTpLspPtPathMepDefects_Type(Bits):
    """Custom type vRtrMplsTpLspPtPathMepDefects based on Bits"""
    namedValues = NamedValues(
        *(("protectionTypeMismatch", 0),
          ("revertModeMismatch", 1))
    )

_VRtrMplsTpLspPtPathMepDefects_Type.__name__ = "Bits"
_VRtrMplsTpLspPtPathMepDefects_Object = MibTableColumn
vRtrMplsTpLspPtPathMepDefects = _VRtrMplsTpLspPtPathMepDefects_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 4, 1, 3),
    _VRtrMplsTpLspPtPathMepDefects_Type()
)
vRtrMplsTpLspPtPathMepDefects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPtPathMepDefects.setStatus("current")
_VRtrMplsTpLspPtPathMepWTRTimer_Type = Counter32
_VRtrMplsTpLspPtPathMepWTRTimer_Object = MibTableColumn
vRtrMplsTpLspPtPathMepWTRTimer = _VRtrMplsTpLspPtPathMepWTRTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 3, 4, 1, 4),
    _VRtrMplsTpLspPtPathMepWTRTimer_Type()
)
vRtrMplsTpLspPtPathMepWTRTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPtPathMepWTRTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMplsTpLspPtPathMepWTRTimer.setUnits("seconds")
_VRtrMplsTpCmdObjects_ObjectIdentity = ObjectIdentity
vRtrMplsTpCmdObjects = _VRtrMplsTpCmdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 4)
)
_VRtrMplsTpTunnelCommandTable_Object = MibTable
vRtrMplsTpTunnelCommandTable = _VRtrMplsTpTunnelCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 4, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelCommandTable.setStatus("current")
_VRtrMplsTpTunnelCommandEntry_Object = MibTableRow
vRtrMplsTpTunnelCommandEntry = _VRtrMplsTpTunnelCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 4, 1, 1)
)
vRtrMplsTpTunnelCommandEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-MIB", "vRtrMplsLspIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelCommandEntry.setStatus("current")


class _VRtrMplsTpTunnelCommandSwitch_Type(Integer32):
    """Custom type vRtrMplsTpTunnelCommandSwitch based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 0),
          ("clear", 1),
          ("forceSwitch", 2),
          ("manualSwitch", 3),
          ("lockout", 4))
    )


_VRtrMplsTpTunnelCommandSwitch_Type.__name__ = "Integer32"
_VRtrMplsTpTunnelCommandSwitch_Object = MibTableColumn
vRtrMplsTpTunnelCommandSwitch = _VRtrMplsTpTunnelCommandSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 4, 1, 1, 1),
    _VRtrMplsTpTunnelCommandSwitch_Type()
)
vRtrMplsTpTunnelCommandSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelCommandSwitch.setStatus("current")
_VRtrMplsTpLsrObjects_ObjectIdentity = ObjectIdentity
vRtrMplsTpLsrObjects = _VRtrMplsTpLsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5)
)
_VRtrMplsTpLsrCfgTable_Object = MibTable
vRtrMplsTpLsrCfgTable = _VRtrMplsTpLsrCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsTpLsrCfgTable.setStatus("current")
_VRtrMplsTpLsrCfgEntry_Object = MibTableRow
vRtrMplsTpLsrCfgEntry = _VRtrMplsTpLsrCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1)
)
vRtrMplsTpLsrCfgEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrPathName"),
)
if mibBuilder.loadTexts:
    vRtrMplsTpLsrCfgEntry.setStatus("current")
_VRtrMplsTpLsrPathName_Type = TNamedItem
_VRtrMplsTpLsrPathName_Object = MibTableColumn
vRtrMplsTpLsrPathName = _VRtrMplsTpLsrPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1, 1),
    _VRtrMplsTpLsrPathName_Type()
)
vRtrMplsTpLsrPathName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrPathName.setStatus("current")
_VRtrMplsTpLsrRowStatus_Type = RowStatus
_VRtrMplsTpLsrRowStatus_Object = MibTableColumn
vRtrMplsTpLsrRowStatus = _VRtrMplsTpLsrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1, 2),
    _VRtrMplsTpLsrRowStatus_Type()
)
vRtrMplsTpLsrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrRowStatus.setStatus("current")
_VRtrMplsTpLsrLastChangedTime_Type = TimeStamp
_VRtrMplsTpLsrLastChangedTime_Object = MibTableColumn
vRtrMplsTpLsrLastChangedTime = _VRtrMplsTpLsrLastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1, 3),
    _VRtrMplsTpLsrLastChangedTime_Type()
)
vRtrMplsTpLsrLastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrLastChangedTime.setStatus("current")


class _VRtrMplsTpLsrAdminState_Type(TmnxAdminState):
    """Custom type vRtrMplsTpLsrAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrMplsTpLsrAdminState_Type.__name__ = "TmnxAdminState"
_VRtrMplsTpLsrAdminState_Object = MibTableColumn
vRtrMplsTpLsrAdminState = _VRtrMplsTpLsrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1, 4),
    _VRtrMplsTpLsrAdminState_Type()
)
vRtrMplsTpLsrAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrAdminState.setStatus("current")
_VRtrMplsTpLsrOperState_Type = TmnxOperState
_VRtrMplsTpLsrOperState_Object = MibTableColumn
vRtrMplsTpLsrOperState = _VRtrMplsTpLsrOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1, 5),
    _VRtrMplsTpLsrOperState_Type()
)
vRtrMplsTpLsrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrOperState.setStatus("current")


class _VRtrMplsTpLsrFPInLabel_Type(Unsigned32):
    """Custom type vRtrMplsTpLsrFPInLabel based on Unsigned32"""
    defaultValue = 0


_VRtrMplsTpLsrFPInLabel_Type.__name__ = "Unsigned32"
_VRtrMplsTpLsrFPInLabel_Object = MibTableColumn
vRtrMplsTpLsrFPInLabel = _VRtrMplsTpLsrFPInLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1, 6),
    _VRtrMplsTpLsrFPInLabel_Type()
)
vRtrMplsTpLsrFPInLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrFPInLabel.setStatus("current")


class _VRtrMplsTpLsrFPOutLabel_Type(Unsigned32):
    """Custom type vRtrMplsTpLsrFPOutLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1048575),
    )


_VRtrMplsTpLsrFPOutLabel_Type.__name__ = "Unsigned32"
_VRtrMplsTpLsrFPOutLabel_Object = MibTableColumn
vRtrMplsTpLsrFPOutLabel = _VRtrMplsTpLsrFPOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1, 7),
    _VRtrMplsTpLsrFPOutLabel_Type()
)
vRtrMplsTpLsrFPOutLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrFPOutLabel.setStatus("current")


class _VRtrMplsTpLsrFPOutLink_Type(InterfaceIndexOrZero):
    """Custom type vRtrMplsTpLsrFPOutLink based on InterfaceIndexOrZero"""
    defaultValue = 0


_VRtrMplsTpLsrFPOutLink_Type.__name__ = "InterfaceIndexOrZero"
_VRtrMplsTpLsrFPOutLink_Object = MibTableColumn
vRtrMplsTpLsrFPOutLink = _VRtrMplsTpLsrFPOutLink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1, 8),
    _VRtrMplsTpLsrFPOutLink_Type()
)
vRtrMplsTpLsrFPOutLink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrFPOutLink.setStatus("current")


class _VRtrMplsTpLsrFPNextHopAddrType_Type(InetAddressType):
    """Custom type vRtrMplsTpLsrFPNextHopAddrType based on InetAddressType"""
    defaultValue = 0


_VRtrMplsTpLsrFPNextHopAddrType_Type.__name__ = "InetAddressType"
_VRtrMplsTpLsrFPNextHopAddrType_Object = MibTableColumn
vRtrMplsTpLsrFPNextHopAddrType = _VRtrMplsTpLsrFPNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1, 9),
    _VRtrMplsTpLsrFPNextHopAddrType_Type()
)
vRtrMplsTpLsrFPNextHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrFPNextHopAddrType.setStatus("current")


class _VRtrMplsTpLsrFPNextHopAddress_Type(InetAddress):
    """Custom type vRtrMplsTpLsrFPNextHopAddress based on InetAddress"""
    defaultValue = OctetString("")

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsTpLsrFPNextHopAddress_Type.__name__ = "InetAddress"
_VRtrMplsTpLsrFPNextHopAddress_Object = MibTableColumn
vRtrMplsTpLsrFPNextHopAddress = _VRtrMplsTpLsrFPNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1, 10),
    _VRtrMplsTpLsrFPNextHopAddress_Type()
)
vRtrMplsTpLsrFPNextHopAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrFPNextHopAddress.setStatus("current")


class _VRtrMplsTpLsrRPInLabel_Type(Unsigned32):
    """Custom type vRtrMplsTpLsrRPInLabel based on Unsigned32"""
    defaultValue = 0


_VRtrMplsTpLsrRPInLabel_Type.__name__ = "Unsigned32"
_VRtrMplsTpLsrRPInLabel_Object = MibTableColumn
vRtrMplsTpLsrRPInLabel = _VRtrMplsTpLsrRPInLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1, 11),
    _VRtrMplsTpLsrRPInLabel_Type()
)
vRtrMplsTpLsrRPInLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrRPInLabel.setStatus("current")


class _VRtrMplsTpLsrRPOutLabel_Type(Unsigned32):
    """Custom type vRtrMplsTpLsrRPOutLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1048575),
    )


_VRtrMplsTpLsrRPOutLabel_Type.__name__ = "Unsigned32"
_VRtrMplsTpLsrRPOutLabel_Object = MibTableColumn
vRtrMplsTpLsrRPOutLabel = _VRtrMplsTpLsrRPOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1, 12),
    _VRtrMplsTpLsrRPOutLabel_Type()
)
vRtrMplsTpLsrRPOutLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrRPOutLabel.setStatus("current")


class _VRtrMplsTpLsrRPOutLink_Type(InterfaceIndexOrZero):
    """Custom type vRtrMplsTpLsrRPOutLink based on InterfaceIndexOrZero"""
    defaultValue = 0


_VRtrMplsTpLsrRPOutLink_Type.__name__ = "InterfaceIndexOrZero"
_VRtrMplsTpLsrRPOutLink_Object = MibTableColumn
vRtrMplsTpLsrRPOutLink = _VRtrMplsTpLsrRPOutLink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1, 13),
    _VRtrMplsTpLsrRPOutLink_Type()
)
vRtrMplsTpLsrRPOutLink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrRPOutLink.setStatus("current")


class _VRtrMplsTpLsrRPNextHopAddrType_Type(InetAddressType):
    """Custom type vRtrMplsTpLsrRPNextHopAddrType based on InetAddressType"""
    defaultValue = 0


_VRtrMplsTpLsrRPNextHopAddrType_Type.__name__ = "InetAddressType"
_VRtrMplsTpLsrRPNextHopAddrType_Object = MibTableColumn
vRtrMplsTpLsrRPNextHopAddrType = _VRtrMplsTpLsrRPNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1, 14),
    _VRtrMplsTpLsrRPNextHopAddrType_Type()
)
vRtrMplsTpLsrRPNextHopAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrRPNextHopAddrType.setStatus("current")


class _VRtrMplsTpLsrRPNextHopAddress_Type(InetAddress):
    """Custom type vRtrMplsTpLsrRPNextHopAddress based on InetAddress"""
    defaultValue = OctetString("")

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrMplsTpLsrRPNextHopAddress_Type.__name__ = "InetAddress"
_VRtrMplsTpLsrRPNextHopAddress_Object = MibTableColumn
vRtrMplsTpLsrRPNextHopAddress = _VRtrMplsTpLsrRPNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1, 15),
    _VRtrMplsTpLsrRPNextHopAddress_Type()
)
vRtrMplsTpLsrRPNextHopAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrRPNextHopAddress.setStatus("current")


class _VRtrMplsTpLsrFPEnabled_Type(TruthValue):
    """Custom type vRtrMplsTpLsrFPEnabled based on TruthValue"""
    defaultValue = 2


_VRtrMplsTpLsrFPEnabled_Type.__name__ = "TruthValue"
_VRtrMplsTpLsrFPEnabled_Object = MibTableColumn
vRtrMplsTpLsrFPEnabled = _VRtrMplsTpLsrFPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1, 16),
    _VRtrMplsTpLsrFPEnabled_Type()
)
vRtrMplsTpLsrFPEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrFPEnabled.setStatus("current")


class _VRtrMplsTpLsrRPEnabled_Type(TruthValue):
    """Custom type vRtrMplsTpLsrRPEnabled based on TruthValue"""
    defaultValue = 2


_VRtrMplsTpLsrRPEnabled_Type.__name__ = "TruthValue"
_VRtrMplsTpLsrRPEnabled_Object = MibTableColumn
vRtrMplsTpLsrRPEnabled = _VRtrMplsTpLsrRPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 1, 1, 17),
    _VRtrMplsTpLsrRPEnabled_Type()
)
vRtrMplsTpLsrRPEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrRPEnabled.setStatus("current")
_VRtrMplsTpLsrPathIdTable_Object = MibTable
vRtrMplsTpLsrPathIdTable = _VRtrMplsTpLsrPathIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 3)
)
if mibBuilder.loadTexts:
    vRtrMplsTpLsrPathIdTable.setStatus("current")
_VRtrMplsTpLsrPathIdEntry_Object = MibTableRow
vRtrMplsTpLsrPathIdEntry = _VRtrMplsTpLsrPathIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 3, 1)
)
vRtrMplsTpLsrPathIdEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrPathIdSrcGlobalId"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrPathIdSrcNodeId"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrPathIdSrcTunNum"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrPathIdDestGlobalId"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrPathIdDestNodeId"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrPathIdDestTunNum"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrPathIdLspNumber"),
)
if mibBuilder.loadTexts:
    vRtrMplsTpLsrPathIdEntry.setStatus("current")
_VRtrMplsTpLsrPathIdSrcGlobalId_Type = TmnxMplsTpGlobalID
_VRtrMplsTpLsrPathIdSrcGlobalId_Object = MibTableColumn
vRtrMplsTpLsrPathIdSrcGlobalId = _VRtrMplsTpLsrPathIdSrcGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 3, 1, 1),
    _VRtrMplsTpLsrPathIdSrcGlobalId_Type()
)
vRtrMplsTpLsrPathIdSrcGlobalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrPathIdSrcGlobalId.setStatus("current")
_VRtrMplsTpLsrPathIdSrcNodeId_Type = TmnxMplsTpNodeID
_VRtrMplsTpLsrPathIdSrcNodeId_Object = MibTableColumn
vRtrMplsTpLsrPathIdSrcNodeId = _VRtrMplsTpLsrPathIdSrcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 3, 1, 2),
    _VRtrMplsTpLsrPathIdSrcNodeId_Type()
)
vRtrMplsTpLsrPathIdSrcNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrPathIdSrcNodeId.setStatus("current")


class _VRtrMplsTpLsrPathIdSrcTunNum_Type(Unsigned32):
    """Custom type vRtrMplsTpLsrPathIdSrcTunNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 61440),
    )


_VRtrMplsTpLsrPathIdSrcTunNum_Type.__name__ = "Unsigned32"
_VRtrMplsTpLsrPathIdSrcTunNum_Object = MibTableColumn
vRtrMplsTpLsrPathIdSrcTunNum = _VRtrMplsTpLsrPathIdSrcTunNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 3, 1, 3),
    _VRtrMplsTpLsrPathIdSrcTunNum_Type()
)
vRtrMplsTpLsrPathIdSrcTunNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrPathIdSrcTunNum.setStatus("current")
_VRtrMplsTpLsrPathIdDestGlobalId_Type = TmnxMplsTpGlobalID
_VRtrMplsTpLsrPathIdDestGlobalId_Object = MibTableColumn
vRtrMplsTpLsrPathIdDestGlobalId = _VRtrMplsTpLsrPathIdDestGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 3, 1, 4),
    _VRtrMplsTpLsrPathIdDestGlobalId_Type()
)
vRtrMplsTpLsrPathIdDestGlobalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrPathIdDestGlobalId.setStatus("current")
_VRtrMplsTpLsrPathIdDestNodeId_Type = TmnxMplsTpNodeID
_VRtrMplsTpLsrPathIdDestNodeId_Object = MibTableColumn
vRtrMplsTpLsrPathIdDestNodeId = _VRtrMplsTpLsrPathIdDestNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 3, 1, 5),
    _VRtrMplsTpLsrPathIdDestNodeId_Type()
)
vRtrMplsTpLsrPathIdDestNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrPathIdDestNodeId.setStatus("current")


class _VRtrMplsTpLsrPathIdDestTunNum_Type(Unsigned32):
    """Custom type vRtrMplsTpLsrPathIdDestTunNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 61440),
    )


_VRtrMplsTpLsrPathIdDestTunNum_Type.__name__ = "Unsigned32"
_VRtrMplsTpLsrPathIdDestTunNum_Object = MibTableColumn
vRtrMplsTpLsrPathIdDestTunNum = _VRtrMplsTpLsrPathIdDestTunNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 3, 1, 6),
    _VRtrMplsTpLsrPathIdDestTunNum_Type()
)
vRtrMplsTpLsrPathIdDestTunNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrPathIdDestTunNum.setStatus("current")


class _VRtrMplsTpLsrPathIdLspNumber_Type(Unsigned32):
    """Custom type vRtrMplsTpLsrPathIdLspNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrMplsTpLsrPathIdLspNumber_Type.__name__ = "Unsigned32"
_VRtrMplsTpLsrPathIdLspNumber_Object = MibTableColumn
vRtrMplsTpLsrPathIdLspNumber = _VRtrMplsTpLsrPathIdLspNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 3, 1, 7),
    _VRtrMplsTpLsrPathIdLspNumber_Type()
)
vRtrMplsTpLsrPathIdLspNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrPathIdLspNumber.setStatus("current")
_VRtrMplsTpLsrPathIdRowStatus_Type = RowStatus
_VRtrMplsTpLsrPathIdRowStatus_Object = MibTableColumn
vRtrMplsTpLsrPathIdRowStatus = _VRtrMplsTpLsrPathIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 3, 1, 8),
    _VRtrMplsTpLsrPathIdRowStatus_Type()
)
vRtrMplsTpLsrPathIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrPathIdRowStatus.setStatus("current")
_VRtrMplsTpLsrPathIdPathName_Type = TNamedItem
_VRtrMplsTpLsrPathIdPathName_Object = MibTableColumn
vRtrMplsTpLsrPathIdPathName = _VRtrMplsTpLsrPathIdPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 3, 1, 9),
    _VRtrMplsTpLsrPathIdPathName_Type()
)
vRtrMplsTpLsrPathIdPathName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrPathIdPathName.setStatus("current")
_VRtrMplsTpLsrMipCfgTable_Object = MibTable
vRtrMplsTpLsrMipCfgTable = _VRtrMplsTpLsrMipCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 4)
)
if mibBuilder.loadTexts:
    vRtrMplsTpLsrMipCfgTable.setStatus("current")
_VRtrMplsTpLsrMipCfgEntry_Object = MibTableRow
vRtrMplsTpLsrMipCfgEntry = _VRtrMplsTpLsrMipCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 4, 1)
)
vRtrMplsTpLsrMipCfgEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrPathName"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrMipDirection"),
)
if mibBuilder.loadTexts:
    vRtrMplsTpLsrMipCfgEntry.setStatus("current")


class _VRtrMplsTpLsrMipDirection_Type(Integer32):
    """Custom type vRtrMplsTpLsrMipDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("reverse", 2))
    )


_VRtrMplsTpLsrMipDirection_Type.__name__ = "Integer32"
_VRtrMplsTpLsrMipDirection_Object = MibTableColumn
vRtrMplsTpLsrMipDirection = _VRtrMplsTpLsrMipDirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 4, 1, 1),
    _VRtrMplsTpLsrMipDirection_Type()
)
vRtrMplsTpLsrMipDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrMipDirection.setStatus("current")
_VRtrMplsTpLsrMipRowStatus_Type = RowStatus
_VRtrMplsTpLsrMipRowStatus_Object = MibTableColumn
vRtrMplsTpLsrMipRowStatus = _VRtrMplsTpLsrMipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 4, 1, 2),
    _VRtrMplsTpLsrMipRowStatus_Type()
)
vRtrMplsTpLsrMipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrMipRowStatus.setStatus("current")
_VRtrMplsTpLsrMipLastChanged_Type = TimeStamp
_VRtrMplsTpLsrMipLastChanged_Object = MibTableColumn
vRtrMplsTpLsrMipLastChanged = _VRtrMplsTpLsrMipLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 4, 1, 3),
    _VRtrMplsTpLsrMipLastChanged_Type()
)
vRtrMplsTpLsrMipLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrMipLastChanged.setStatus("current")


class _VRtrMplsTpLsrMipDSInIfNum_Type(Unsigned32):
    """Custom type vRtrMplsTpLsrMipDSInIfNum based on Unsigned32"""
    defaultValue = 0


_VRtrMplsTpLsrMipDSInIfNum_Type.__name__ = "Unsigned32"
_VRtrMplsTpLsrMipDSInIfNum_Object = MibTableColumn
vRtrMplsTpLsrMipDSInIfNum = _VRtrMplsTpLsrMipDSInIfNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 4, 1, 4),
    _VRtrMplsTpLsrMipDSInIfNum_Type()
)
vRtrMplsTpLsrMipDSInIfNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrMipDSInIfNum.setStatus("current")


class _VRtrMplsTpLsrMipDSOutIfNum_Type(Unsigned32):
    """Custom type vRtrMplsTpLsrMipDSOutIfNum based on Unsigned32"""
    defaultValue = 0


_VRtrMplsTpLsrMipDSOutIfNum_Type.__name__ = "Unsigned32"
_VRtrMplsTpLsrMipDSOutIfNum_Object = MibTableColumn
vRtrMplsTpLsrMipDSOutIfNum = _VRtrMplsTpLsrMipDSOutIfNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 5, 4, 1, 5),
    _VRtrMplsTpLsrMipDSOutIfNum_Type()
)
vRtrMplsTpLsrMipDSOutIfNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpLsrMipDSOutIfNum.setStatus("current")
_VRtrMplsTpInterfaceObjects_ObjectIdentity = ObjectIdentity
vRtrMplsTpInterfaceObjects = _VRtrMplsTpInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 6)
)
_VRtrMplsTpIfCfgTable_Object = MibTable
vRtrMplsTpIfCfgTable = _VRtrMplsTpIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 6, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsTpIfCfgTable.setStatus("current")
_VRtrMplsTpIfCfgEntry_Object = MibTableRow
vRtrMplsTpIfCfgEntry = _VRtrMplsTpIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 6, 1, 1)
)
vRtrMplsTpIfCfgEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrMplsTpIfCfgEntry.setStatus("current")
_VRtrMplsTpIfRowStatus_Type = RowStatus
_VRtrMplsTpIfRowStatus_Object = MibTableColumn
vRtrMplsTpIfRowStatus = _VRtrMplsTpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 6, 1, 1, 1),
    _VRtrMplsTpIfRowStatus_Type()
)
vRtrMplsTpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpIfRowStatus.setStatus("current")
_VRtrMplsTpIfLastChanged_Type = TimeStamp
_VRtrMplsTpIfLastChanged_Object = MibTableColumn
vRtrMplsTpIfLastChanged = _VRtrMplsTpIfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 6, 1, 1, 2),
    _VRtrMplsTpIfLastChanged_Type()
)
vRtrMplsTpIfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpIfLastChanged.setStatus("current")


class _VRtrMplsTpIfNum_Type(Unsigned32):
    """Custom type vRtrMplsTpIfNum based on Unsigned32"""
    defaultValue = 0


_VRtrMplsTpIfNum_Type.__name__ = "Unsigned32"
_VRtrMplsTpIfNum_Object = MibTableColumn
vRtrMplsTpIfNum = _VRtrMplsTpIfNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 6, 1, 1, 3),
    _VRtrMplsTpIfNum_Type()
)
vRtrMplsTpIfNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpIfNum.setStatus("current")


class _VRtrMplsTpIfNumValidation_Type(TmnxEnabledDisabled):
    """Custom type vRtrMplsTpIfNumValidation based on TmnxEnabledDisabled"""
    defaultValue = 1


_VRtrMplsTpIfNumValidation_Type.__name__ = "TmnxEnabledDisabled"
_VRtrMplsTpIfNumValidation_Object = MibTableColumn
vRtrMplsTpIfNumValidation = _VRtrMplsTpIfNumValidation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 2, 6, 1, 1, 4),
    _VRtrMplsTpIfNumValidation_Type()
)
vRtrMplsTpIfNumValidation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsTpIfNumValidation.setStatus("current")
_VRtrMplsTpStatus_ObjectIdentity = ObjectIdentity
vRtrMplsTpStatus = _VRtrMplsTpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 3)
)
_VRtrMplsTpStatusObjects_ObjectIdentity = ObjectIdentity
vRtrMplsTpStatusObjects = _VRtrMplsTpStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 3, 1)
)
_VRtrMplsTpTunnelTable_Object = MibTable
vRtrMplsTpTunnelTable = _VRtrMplsTpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 3, 1, 1)
)
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelTable.setStatus("current")
_VRtrMplsTpTunnelEntry_Object = MibTableRow
vRtrMplsTpTunnelEntry = _VRtrMplsTpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 3, 1, 1, 1)
)
vRtrMplsTpTunnelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpTunnelNodeId"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpTunnelGlobalId"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpTunnelPreference"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpTunnelType"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpTunnelID"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpTunnelNextHopAddrType"),
    (0, "TIMETRA-MPLS-TP-MIB", "vRtrMplsTpTunnelNextHopAddress"),
)
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelEntry.setStatus("current")
_VRtrMplsTpTunnelNodeId_Type = TmnxMplsTpNodeID
_VRtrMplsTpTunnelNodeId_Object = MibTableColumn
vRtrMplsTpTunnelNodeId = _VRtrMplsTpTunnelNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 3, 1, 1, 1, 1),
    _VRtrMplsTpTunnelNodeId_Type()
)
vRtrMplsTpTunnelNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelNodeId.setStatus("current")
_VRtrMplsTpTunnelGlobalId_Type = TmnxMplsTpGlobalID
_VRtrMplsTpTunnelGlobalId_Object = MibTableColumn
vRtrMplsTpTunnelGlobalId = _VRtrMplsTpTunnelGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 3, 1, 1, 1, 2),
    _VRtrMplsTpTunnelGlobalId_Type()
)
vRtrMplsTpTunnelGlobalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelGlobalId.setStatus("current")


class _VRtrMplsTpTunnelPreference_Type(Unsigned32):
    """Custom type vRtrMplsTpTunnelPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrMplsTpTunnelPreference_Type.__name__ = "Unsigned32"
_VRtrMplsTpTunnelPreference_Object = MibTableColumn
vRtrMplsTpTunnelPreference = _VRtrMplsTpTunnelPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 3, 1, 1, 1, 3),
    _VRtrMplsTpTunnelPreference_Type()
)
vRtrMplsTpTunnelPreference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelPreference.setStatus("current")
_VRtrMplsTpTunnelType_Type = TmnxMplsTpTunnelType
_VRtrMplsTpTunnelType_Object = MibTableColumn
vRtrMplsTpTunnelType = _VRtrMplsTpTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 3, 1, 1, 1, 4),
    _VRtrMplsTpTunnelType_Type()
)
vRtrMplsTpTunnelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelType.setStatus("current")
_VRtrMplsTpTunnelID_Type = TmnxTunnelID
_VRtrMplsTpTunnelID_Object = MibTableColumn
vRtrMplsTpTunnelID = _VRtrMplsTpTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 3, 1, 1, 1, 5),
    _VRtrMplsTpTunnelID_Type()
)
vRtrMplsTpTunnelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelID.setStatus("current")
_VRtrMplsTpTunnelNextHopAddrType_Type = InetAddressType
_VRtrMplsTpTunnelNextHopAddrType_Object = MibTableColumn
vRtrMplsTpTunnelNextHopAddrType = _VRtrMplsTpTunnelNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 3, 1, 1, 1, 6),
    _VRtrMplsTpTunnelNextHopAddrType_Type()
)
vRtrMplsTpTunnelNextHopAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelNextHopAddrType.setStatus("current")


class _VRtrMplsTpTunnelNextHopAddress_Type(InetAddress):
    """Custom type vRtrMplsTpTunnelNextHopAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_VRtrMplsTpTunnelNextHopAddress_Type.__name__ = "InetAddress"
_VRtrMplsTpTunnelNextHopAddress_Object = MibTableColumn
vRtrMplsTpTunnelNextHopAddress = _VRtrMplsTpTunnelNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 3, 1, 1, 1, 7),
    _VRtrMplsTpTunnelNextHopAddress_Type()
)
vRtrMplsTpTunnelNextHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelNextHopAddress.setStatus("current")
_VRtrMplsTpTunnelMetric_Type = Unsigned32
_VRtrMplsTpTunnelMetric_Object = MibTableColumn
vRtrMplsTpTunnelMetric = _VRtrMplsTpTunnelMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 3, 1, 1, 1, 8),
    _VRtrMplsTpTunnelMetric_Type()
)
vRtrMplsTpTunnelMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelMetric.setStatus("current")
_VRtrMplsTpTunnelAge_Type = Integer32
_VRtrMplsTpTunnelAge_Object = MibTableColumn
vRtrMplsTpTunnelAge = _VRtrMplsTpTunnelAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 3, 1, 1, 1, 9),
    _VRtrMplsTpTunnelAge_Type()
)
vRtrMplsTpTunnelAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelAge.setStatus("current")
_VRtrMplsTpStatistics_ObjectIdentity = ObjectIdentity
vRtrMplsTpStatistics = _VRtrMplsTpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 5)
)
_VRtrMplsTpActions_ObjectIdentity = ObjectIdentity
vRtrMplsTpActions = _VRtrMplsTpActions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 6)
)
_VRtrMplsTpNotifyObjects_ObjectIdentity = ObjectIdentity
vRtrMplsTpNotifyObjects = _VRtrMplsTpNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 10)
)


class _VRtrMplsTpLspOldPathIndex_Type(Integer32):
    """Custom type vRtrMplsTpLspOldPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("working", 1),
          ("protecting", 2))
    )


_VRtrMplsTpLspOldPathIndex_Type.__name__ = "Integer32"
_VRtrMplsTpLspOldPathIndex_Object = MibScalar
vRtrMplsTpLspOldPathIndex = _VRtrMplsTpLspOldPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 83, 10, 1),
    _VRtrMplsTpLspOldPathIndex_Type()
)
vRtrMplsTpLspOldPathIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrMplsTpLspOldPathIndex.setStatus("current")
_VRtrMplsTpNotifyPrefix_ObjectIdentity = ObjectIdentity
vRtrMplsTpNotifyPrefix = _VRtrMplsTpNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 83)
)
_VRtrMplsTpNotifications_ObjectIdentity = ObjectIdentity
vRtrMplsTpNotifications = _VRtrMplsTpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 83, 0)
)

# Managed Objects groups

vRtrMplsTpTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2, 1, 1)
)
vRtrMplsTpTimeStampGroup.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpSystemTableLastChanged"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpOamTemplTblLastChanged"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpPtcTemplTblLastChanged"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathTblLastChanged"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathMepTblLastChg"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrPathIdTblLastChg"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrTblLastChanged"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpTimeStampGroup.setStatus("current")

vRtrMplsTpSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2, 1, 2)
)
vRtrMplsTpSystemGroup.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpRowStatus"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpGlobalId"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpNodeId"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpTunnelIdMin"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpTunnelIdMax"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpAdminState"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpInheritance"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpSystemGroup.setStatus("current")

vRtrMplsTpOamTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2, 1, 3)
)
vRtrMplsTpOamTemplateGroup.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpOamTmplRowStatus"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpOamTmplLastChangedTime"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpOamTmplBfdTemplateName"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpOamTmplHoldTimeDown"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpOamTmplHoldTimeUp"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpOamTemplateGroup.setStatus("current")

vRtrMplsTpProtectionTemplGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2, 1, 4)
)
vRtrMplsTpProtectionTemplGroup.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpPtcTmplRowStatus"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpPtcTmplLastChangedTime"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpPtcTmplProtectionMode"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpPtcTmplProtectionDir"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpPtcTmplRevertive"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpPtcTmplWaitToRestore"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpPtcTmplRapidPscTimer"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpPtcTmplSlowPscTimer"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpProtectionTemplGroup.setStatus("current")

vRtrMplsTpLspPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2, 1, 5)
)
vRtrMplsTpLspPathGroup.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathRowStatus"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathLastChangedTime"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathAdminState"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathOperState"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathReasonDownFlags"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathLspNumber"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathInLabel"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathOutLabel"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathOutLink"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathNextHopAddrType"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathNextHopAddress"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathState"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathTimeUp"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathTimeDown"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathActiveTimeUp"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathGroup.setStatus("current")

vRtrMplsTpLspPathMepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2, 1, 6)
)
vRtrMplsTpLspPathMepGroup.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathMepLastChgTime"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathMepRowStatus"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathMepAdminState"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathMepProtectTmpl"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathMepOamTmpl"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathMepBfdEnabled"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathMepBfdOperState"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPtPathMepRxPdu"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPtPathMepTxPdu"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPtPathMepDefects"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPtPathMepWTRTimer"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathMepGroup.setStatus("current")

vRtrMplsTpTunnelCommandGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2, 1, 7)
)
vRtrMplsTpTunnelCommandGroup.setObjects(
    ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpTunnelCommandSwitch")
)
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelCommandGroup.setStatus("current")

vRtrMplsTpTunnelTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2, 1, 8)
)
vRtrMplsTpTunnelTableGroup.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpTunnelMetric"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpTunnelAge"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpTunnelTableGroup.setStatus("current")

vRtrMplsTpLsrCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2, 1, 9)
)
vRtrMplsTpLsrCfgGroup.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrRowStatus"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrLastChangedTime"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrAdminState"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrOperState"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrFPInLabel"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrFPOutLabel"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrFPOutLink"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrFPNextHopAddrType"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrFPNextHopAddress"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrRPInLabel"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrRPOutLabel"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrRPOutLink"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrRPNextHopAddrType"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrRPNextHopAddress"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrFPEnabled"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrRPEnabled"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpLsrCfgGroup.setStatus("current")

vRtrMplsTpLsrPathIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2, 1, 10)
)
vRtrMplsTpLsrPathIdGroup.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrPathIdRowStatus"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrPathIdPathName"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpLsrPathIdGroup.setStatus("current")

vRtrMplsTpNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2, 1, 12)
)
vRtrMplsTpNotifyObjsGroup.setObjects(
    ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspOldPathIndex")
)
if mibBuilder.loadTexts:
    vRtrMplsTpNotifyObjsGroup.setStatus("current")

vRtrMplsTpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2, 2, 1)
)
vRtrMplsTpInterfaceGroup.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpIfTblLastChanged"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpIfRowStatus"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpIfLastChanged"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpIfNum"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpIfNumValidation"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpInterfaceGroup.setStatus("current")

vRtrMplsTpLsrMipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2, 2, 2)
)
vRtrMplsTpLsrMipGroup.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrMipCfgTblLastChg"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrMipRowStatus"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrMipLastChanged"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrMipDSInIfNum"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrMipDSOutIfNum"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpLsrMipGroup.setStatus("current")

vRtrMplsTpLspPathMepV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2, 2, 3)
)
vRtrMplsTpLspPathMepV12v0Group.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathMepDSInIfNum"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathMepDSOutIfNum"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpLspPathMepV12v0Group.setStatus("current")


# Notification objects

vRtrMplsTpLspRevertMismatchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 83, 0, 1)
)
vRtrMplsTpLspRevertMismatchAlarm.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPtPathMepRxPdu"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPtPathMepTxPdu"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpLspRevertMismatchAlarm.setStatus(
        "current"
    )

vRtrMplsTpLspRevertMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 83, 0, 2)
)
vRtrMplsTpLspRevertMismatchClear.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPtPathMepRxPdu"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPtPathMepTxPdu"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpLspRevertMismatchClear.setStatus(
        "current"
    )

vRtrMplsTpLspPtTypeMismatchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 83, 0, 3)
)
vRtrMplsTpLspPtTypeMismatchAlarm.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPtPathMepRxPdu"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPtPathMepTxPdu"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpLspPtTypeMismatchAlarm.setStatus(
        "current"
    )

vRtrMplsTpLspPtTypeMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 83, 0, 4)
)
vRtrMplsTpLspPtTypeMismatchClear.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPtPathMepRxPdu"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPtPathMepTxPdu"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpLspPtTypeMismatchClear.setStatus(
        "current"
    )

vRtrMplsTpLspActivePathUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 83, 0, 5)
)
vRtrMplsTpLspActivePathUp.setObjects(
    ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathState")
)
if mibBuilder.loadTexts:
    vRtrMplsTpLspActivePathUp.setStatus(
        "current"
    )

vRtrMplsTpLspActivePathChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 83, 0, 6)
)
vRtrMplsTpLspActivePathChange.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathState"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspOldPathIndex"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpLspActivePathChange.setStatus(
        "current"
    )


# Notifications groups

vRtrMplsTpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 2, 1, 11)
)
vRtrMplsTpNotificationGroup.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspRevertMismatchAlarm"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspRevertMismatchClear"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPtTypeMismatchAlarm"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPtTypeMismatchClear"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspActivePathUp"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspActivePathChange"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vRtrMplsTpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 1, 1)
)
vRtrMplsTpCompliance.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpTimeStampGroup"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpSystemGroup"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpOamTemplateGroup"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpProtectionTemplGroup"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathGroup"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathMepGroup"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpTunnelCommandGroup"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpTunnelTableGroup"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrCfgGroup"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrPathIdGroup"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpNotificationGroup"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpNotifyObjsGroup"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpCompliance.setStatus(
        "current"
    )

vRtrMplsTpV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 83, 1, 2)
)
vRtrMplsTpV12v0Compliance.setObjects(
      *(("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpInterfaceGroup"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLsrMipGroup"),
        ("TIMETRA-MPLS-TP-MIB", "vRtrMplsTpLspPathMepV12v0Group"))
)
if mibBuilder.loadTexts:
    vRtrMplsTpV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-MPLS-TP-MIB",
    **{"VRtrMplsTpLspPathMepPduType": VRtrMplsTpLspPathMepPduType,
       "timetraMplsTpMIBModule": timetraMplsTpMIBModule,
       "vRtrMplsTpConformance": vRtrMplsTpConformance,
       "vRtrMplsTpCompliances": vRtrMplsTpCompliances,
       "vRtrMplsTpCompliance": vRtrMplsTpCompliance,
       "vRtrMplsTpV12v0Compliance": vRtrMplsTpV12v0Compliance,
       "vRtrMplsTpGroups": vRtrMplsTpGroups,
       "vRtrMplsTpV11v0Groups": vRtrMplsTpV11v0Groups,
       "vRtrMplsTpTimeStampGroup": vRtrMplsTpTimeStampGroup,
       "vRtrMplsTpSystemGroup": vRtrMplsTpSystemGroup,
       "vRtrMplsTpOamTemplateGroup": vRtrMplsTpOamTemplateGroup,
       "vRtrMplsTpProtectionTemplGroup": vRtrMplsTpProtectionTemplGroup,
       "vRtrMplsTpLspPathGroup": vRtrMplsTpLspPathGroup,
       "vRtrMplsTpLspPathMepGroup": vRtrMplsTpLspPathMepGroup,
       "vRtrMplsTpTunnelCommandGroup": vRtrMplsTpTunnelCommandGroup,
       "vRtrMplsTpTunnelTableGroup": vRtrMplsTpTunnelTableGroup,
       "vRtrMplsTpLsrCfgGroup": vRtrMplsTpLsrCfgGroup,
       "vRtrMplsTpLsrPathIdGroup": vRtrMplsTpLsrPathIdGroup,
       "vRtrMplsTpNotificationGroup": vRtrMplsTpNotificationGroup,
       "vRtrMplsTpNotifyObjsGroup": vRtrMplsTpNotifyObjsGroup,
       "vRtrMplsTpV12v0Groups": vRtrMplsTpV12v0Groups,
       "vRtrMplsTpInterfaceGroup": vRtrMplsTpInterfaceGroup,
       "vRtrMplsTpLsrMipGroup": vRtrMplsTpLsrMipGroup,
       "vRtrMplsTpLspPathMepV12v0Group": vRtrMplsTpLspPathMepV12v0Group,
       "vRtrMplsTpObjs": vRtrMplsTpObjs,
       "vRtrMplsTpConfigTimeStamps": vRtrMplsTpConfigTimeStamps,
       "vRtrMplsTpSystemTableLastChanged": vRtrMplsTpSystemTableLastChanged,
       "vRtrMplsTpOamTemplTblLastChanged": vRtrMplsTpOamTemplTblLastChanged,
       "vRtrMplsTpPtcTemplTblLastChanged": vRtrMplsTpPtcTemplTblLastChanged,
       "vRtrMplsTpLspPathTblLastChanged": vRtrMplsTpLspPathTblLastChanged,
       "vRtrMplsTpLspPathMepTblLastChg": vRtrMplsTpLspPathMepTblLastChg,
       "vRtrMplsTpLsrTblLastChanged": vRtrMplsTpLsrTblLastChanged,
       "vRtrMplsTpLsrPathIdTblLastChg": vRtrMplsTpLsrPathIdTblLastChg,
       "vRtrMplsTpLsrMipCfgTblLastChg": vRtrMplsTpLsrMipCfgTblLastChg,
       "vRtrMplsTpIfTblLastChanged": vRtrMplsTpIfTblLastChanged,
       "vRtrMplsTpConfigurations": vRtrMplsTpConfigurations,
       "vRtrMplsTpSystemIdentifiers": vRtrMplsTpSystemIdentifiers,
       "vRtrMplsTpSystemTable": vRtrMplsTpSystemTable,
       "vRtrMplsTpSystemEntry": vRtrMplsTpSystemEntry,
       "vRtrMplsTpRowStatus": vRtrMplsTpRowStatus,
       "vRtrMplsTpGlobalId": vRtrMplsTpGlobalId,
       "vRtrMplsTpNodeId": vRtrMplsTpNodeId,
       "vRtrMplsTpTunnelIdMin": vRtrMplsTpTunnelIdMin,
       "vRtrMplsTpTunnelIdMax": vRtrMplsTpTunnelIdMax,
       "vRtrMplsTpAdminState": vRtrMplsTpAdminState,
       "vRtrMplsTpInheritance": vRtrMplsTpInheritance,
       "vRtrMplsTpTemplateObjects": vRtrMplsTpTemplateObjects,
       "vRtrMplsTpOamTemplateCfgTable": vRtrMplsTpOamTemplateCfgTable,
       "vRtrMplsTpOamTemplateCfgEntry": vRtrMplsTpOamTemplateCfgEntry,
       "vRtrMplsTpOamTmplName": vRtrMplsTpOamTmplName,
       "vRtrMplsTpOamTmplRowStatus": vRtrMplsTpOamTmplRowStatus,
       "vRtrMplsTpOamTmplLastChangedTime": vRtrMplsTpOamTmplLastChangedTime,
       "vRtrMplsTpOamTmplBfdTemplateName": vRtrMplsTpOamTmplBfdTemplateName,
       "vRtrMplsTpOamTmplHoldTimeDown": vRtrMplsTpOamTmplHoldTimeDown,
       "vRtrMplsTpOamTmplHoldTimeUp": vRtrMplsTpOamTmplHoldTimeUp,
       "vRtrMplsTpPtcTemplateCfgTable": vRtrMplsTpPtcTemplateCfgTable,
       "vRtrMplsTpPtcTemplateCfgEntry": vRtrMplsTpPtcTemplateCfgEntry,
       "vRtrMplsTpPtcTmplName": vRtrMplsTpPtcTmplName,
       "vRtrMplsTpPtcTmplRowStatus": vRtrMplsTpPtcTmplRowStatus,
       "vRtrMplsTpPtcTmplLastChangedTime": vRtrMplsTpPtcTmplLastChangedTime,
       "vRtrMplsTpPtcTmplProtectionMode": vRtrMplsTpPtcTmplProtectionMode,
       "vRtrMplsTpPtcTmplProtectionDir": vRtrMplsTpPtcTmplProtectionDir,
       "vRtrMplsTpPtcTmplRevertive": vRtrMplsTpPtcTmplRevertive,
       "vRtrMplsTpPtcTmplWaitToRestore": vRtrMplsTpPtcTmplWaitToRestore,
       "vRtrMplsTpPtcTmplRapidPscTimer": vRtrMplsTpPtcTmplRapidPscTimer,
       "vRtrMplsTpPtcTmplSlowPscTimer": vRtrMplsTpPtcTmplSlowPscTimer,
       "vRtrMplsTpLspObjects": vRtrMplsTpLspObjects,
       "vRtrMplsTpLspPathTable": vRtrMplsTpLspPathTable,
       "vRtrMplsTpLspPathEntry": vRtrMplsTpLspPathEntry,
       "vRtrMplsTpLspPathIndex": vRtrMplsTpLspPathIndex,
       "vRtrMplsTpLspPathRowStatus": vRtrMplsTpLspPathRowStatus,
       "vRtrMplsTpLspPathLastChangedTime": vRtrMplsTpLspPathLastChangedTime,
       "vRtrMplsTpLspPathAdminState": vRtrMplsTpLspPathAdminState,
       "vRtrMplsTpLspPathOperState": vRtrMplsTpLspPathOperState,
       "vRtrMplsTpLspPathReasonDownFlags": vRtrMplsTpLspPathReasonDownFlags,
       "vRtrMplsTpLspPathLspNumber": vRtrMplsTpLspPathLspNumber,
       "vRtrMplsTpLspPathInLabel": vRtrMplsTpLspPathInLabel,
       "vRtrMplsTpLspPathOutLabel": vRtrMplsTpLspPathOutLabel,
       "vRtrMplsTpLspPathOutLink": vRtrMplsTpLspPathOutLink,
       "vRtrMplsTpLspPathNextHopAddrType": vRtrMplsTpLspPathNextHopAddrType,
       "vRtrMplsTpLspPathNextHopAddress": vRtrMplsTpLspPathNextHopAddress,
       "vRtrMplsTpLspPathState": vRtrMplsTpLspPathState,
       "vRtrMplsTpLspPathTimeUp": vRtrMplsTpLspPathTimeUp,
       "vRtrMplsTpLspPathTimeDown": vRtrMplsTpLspPathTimeDown,
       "vRtrMplsTpLspPathActiveTimeUp": vRtrMplsTpLspPathActiveTimeUp,
       "vRtrMplsTpLspPathMepTable": vRtrMplsTpLspPathMepTable,
       "vRtrMplsTpLspPathMepEntry": vRtrMplsTpLspPathMepEntry,
       "vRtrMplsTpLspPathMepLastChgTime": vRtrMplsTpLspPathMepLastChgTime,
       "vRtrMplsTpLspPathMepRowStatus": vRtrMplsTpLspPathMepRowStatus,
       "vRtrMplsTpLspPathMepAdminState": vRtrMplsTpLspPathMepAdminState,
       "vRtrMplsTpLspPathMepProtectTmpl": vRtrMplsTpLspPathMepProtectTmpl,
       "vRtrMplsTpLspPathMepOamTmpl": vRtrMplsTpLspPathMepOamTmpl,
       "vRtrMplsTpLspPathMepBfdEnabled": vRtrMplsTpLspPathMepBfdEnabled,
       "vRtrMplsTpLspPathMepBfdOperState": vRtrMplsTpLspPathMepBfdOperState,
       "vRtrMplsTpLspPathMepDSInIfNum": vRtrMplsTpLspPathMepDSInIfNum,
       "vRtrMplsTpLspPathMepDSOutIfNum": vRtrMplsTpLspPathMepDSOutIfNum,
       "vRtrMplsTpLspPtPathMepStatTable": vRtrMplsTpLspPtPathMepStatTable,
       "vRtrMplsTpLspPtPathMepStatEntry": vRtrMplsTpLspPtPathMepStatEntry,
       "vRtrMplsTpLspPtPathMepRxPdu": vRtrMplsTpLspPtPathMepRxPdu,
       "vRtrMplsTpLspPtPathMepTxPdu": vRtrMplsTpLspPtPathMepTxPdu,
       "vRtrMplsTpLspPtPathMepDefects": vRtrMplsTpLspPtPathMepDefects,
       "vRtrMplsTpLspPtPathMepWTRTimer": vRtrMplsTpLspPtPathMepWTRTimer,
       "vRtrMplsTpCmdObjects": vRtrMplsTpCmdObjects,
       "vRtrMplsTpTunnelCommandTable": vRtrMplsTpTunnelCommandTable,
       "vRtrMplsTpTunnelCommandEntry": vRtrMplsTpTunnelCommandEntry,
       "vRtrMplsTpTunnelCommandSwitch": vRtrMplsTpTunnelCommandSwitch,
       "vRtrMplsTpLsrObjects": vRtrMplsTpLsrObjects,
       "vRtrMplsTpLsrCfgTable": vRtrMplsTpLsrCfgTable,
       "vRtrMplsTpLsrCfgEntry": vRtrMplsTpLsrCfgEntry,
       "vRtrMplsTpLsrPathName": vRtrMplsTpLsrPathName,
       "vRtrMplsTpLsrRowStatus": vRtrMplsTpLsrRowStatus,
       "vRtrMplsTpLsrLastChangedTime": vRtrMplsTpLsrLastChangedTime,
       "vRtrMplsTpLsrAdminState": vRtrMplsTpLsrAdminState,
       "vRtrMplsTpLsrOperState": vRtrMplsTpLsrOperState,
       "vRtrMplsTpLsrFPInLabel": vRtrMplsTpLsrFPInLabel,
       "vRtrMplsTpLsrFPOutLabel": vRtrMplsTpLsrFPOutLabel,
       "vRtrMplsTpLsrFPOutLink": vRtrMplsTpLsrFPOutLink,
       "vRtrMplsTpLsrFPNextHopAddrType": vRtrMplsTpLsrFPNextHopAddrType,
       "vRtrMplsTpLsrFPNextHopAddress": vRtrMplsTpLsrFPNextHopAddress,
       "vRtrMplsTpLsrRPInLabel": vRtrMplsTpLsrRPInLabel,
       "vRtrMplsTpLsrRPOutLabel": vRtrMplsTpLsrRPOutLabel,
       "vRtrMplsTpLsrRPOutLink": vRtrMplsTpLsrRPOutLink,
       "vRtrMplsTpLsrRPNextHopAddrType": vRtrMplsTpLsrRPNextHopAddrType,
       "vRtrMplsTpLsrRPNextHopAddress": vRtrMplsTpLsrRPNextHopAddress,
       "vRtrMplsTpLsrFPEnabled": vRtrMplsTpLsrFPEnabled,
       "vRtrMplsTpLsrRPEnabled": vRtrMplsTpLsrRPEnabled,
       "vRtrMplsTpLsrPathIdTable": vRtrMplsTpLsrPathIdTable,
       "vRtrMplsTpLsrPathIdEntry": vRtrMplsTpLsrPathIdEntry,
       "vRtrMplsTpLsrPathIdSrcGlobalId": vRtrMplsTpLsrPathIdSrcGlobalId,
       "vRtrMplsTpLsrPathIdSrcNodeId": vRtrMplsTpLsrPathIdSrcNodeId,
       "vRtrMplsTpLsrPathIdSrcTunNum": vRtrMplsTpLsrPathIdSrcTunNum,
       "vRtrMplsTpLsrPathIdDestGlobalId": vRtrMplsTpLsrPathIdDestGlobalId,
       "vRtrMplsTpLsrPathIdDestNodeId": vRtrMplsTpLsrPathIdDestNodeId,
       "vRtrMplsTpLsrPathIdDestTunNum": vRtrMplsTpLsrPathIdDestTunNum,
       "vRtrMplsTpLsrPathIdLspNumber": vRtrMplsTpLsrPathIdLspNumber,
       "vRtrMplsTpLsrPathIdRowStatus": vRtrMplsTpLsrPathIdRowStatus,
       "vRtrMplsTpLsrPathIdPathName": vRtrMplsTpLsrPathIdPathName,
       "vRtrMplsTpLsrMipCfgTable": vRtrMplsTpLsrMipCfgTable,
       "vRtrMplsTpLsrMipCfgEntry": vRtrMplsTpLsrMipCfgEntry,
       "vRtrMplsTpLsrMipDirection": vRtrMplsTpLsrMipDirection,
       "vRtrMplsTpLsrMipRowStatus": vRtrMplsTpLsrMipRowStatus,
       "vRtrMplsTpLsrMipLastChanged": vRtrMplsTpLsrMipLastChanged,
       "vRtrMplsTpLsrMipDSInIfNum": vRtrMplsTpLsrMipDSInIfNum,
       "vRtrMplsTpLsrMipDSOutIfNum": vRtrMplsTpLsrMipDSOutIfNum,
       "vRtrMplsTpInterfaceObjects": vRtrMplsTpInterfaceObjects,
       "vRtrMplsTpIfCfgTable": vRtrMplsTpIfCfgTable,
       "vRtrMplsTpIfCfgEntry": vRtrMplsTpIfCfgEntry,
       "vRtrMplsTpIfRowStatus": vRtrMplsTpIfRowStatus,
       "vRtrMplsTpIfLastChanged": vRtrMplsTpIfLastChanged,
       "vRtrMplsTpIfNum": vRtrMplsTpIfNum,
       "vRtrMplsTpIfNumValidation": vRtrMplsTpIfNumValidation,
       "vRtrMplsTpStatus": vRtrMplsTpStatus,
       "vRtrMplsTpStatusObjects": vRtrMplsTpStatusObjects,
       "vRtrMplsTpTunnelTable": vRtrMplsTpTunnelTable,
       "vRtrMplsTpTunnelEntry": vRtrMplsTpTunnelEntry,
       "vRtrMplsTpTunnelNodeId": vRtrMplsTpTunnelNodeId,
       "vRtrMplsTpTunnelGlobalId": vRtrMplsTpTunnelGlobalId,
       "vRtrMplsTpTunnelPreference": vRtrMplsTpTunnelPreference,
       "vRtrMplsTpTunnelType": vRtrMplsTpTunnelType,
       "vRtrMplsTpTunnelID": vRtrMplsTpTunnelID,
       "vRtrMplsTpTunnelNextHopAddrType": vRtrMplsTpTunnelNextHopAddrType,
       "vRtrMplsTpTunnelNextHopAddress": vRtrMplsTpTunnelNextHopAddress,
       "vRtrMplsTpTunnelMetric": vRtrMplsTpTunnelMetric,
       "vRtrMplsTpTunnelAge": vRtrMplsTpTunnelAge,
       "vRtrMplsTpStatistics": vRtrMplsTpStatistics,
       "vRtrMplsTpActions": vRtrMplsTpActions,
       "vRtrMplsTpNotifyObjects": vRtrMplsTpNotifyObjects,
       "vRtrMplsTpLspOldPathIndex": vRtrMplsTpLspOldPathIndex,
       "vRtrMplsTpNotifyPrefix": vRtrMplsTpNotifyPrefix,
       "vRtrMplsTpNotifications": vRtrMplsTpNotifications,
       "vRtrMplsTpLspRevertMismatchAlarm": vRtrMplsTpLspRevertMismatchAlarm,
       "vRtrMplsTpLspRevertMismatchClear": vRtrMplsTpLspRevertMismatchClear,
       "vRtrMplsTpLspPtTypeMismatchAlarm": vRtrMplsTpLspPtTypeMismatchAlarm,
       "vRtrMplsTpLspPtTypeMismatchClear": vRtrMplsTpLspPtTypeMismatchClear,
       "vRtrMplsTpLspActivePathUp": vRtrMplsTpLspActivePathUp,
       "vRtrMplsTpLspActivePathChange": vRtrMplsTpLspActivePathChange}
)
