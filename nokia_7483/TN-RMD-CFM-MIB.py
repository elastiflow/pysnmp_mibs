# SNMP MIB module (TN-RMD-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TN-RMD-CFM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:08:44 2025
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

(Dot1agCfmCcmInterval,
 Dot1agCfmMDLevel,
 Dot1agCfmMaintAssocName,
 Dot1agCfmMaintAssocNameType,
 Dot1agCfmMaintDomainName,
 Dot1agCfmMaintDomainNameType,
 Dot1agCfmMepId,
 Dot1agCfmMpDirection,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmCcmInterval",
    "Dot1agCfmMDLevel",
    "Dot1agCfmMaintAssocName",
    "Dot1agCfmMaintAssocNameType",
    "Dot1agCfmMaintDomainName",
    "Dot1agCfmMaintDomainNameType",
    "Dot1agCfmMepId",
    "Dot1agCfmMpDirection",
    "VlanIdOrNone")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

(tnRmdSystemId,) = mibBuilder.importSymbols(
    "TN-RMD-SYSTEM-MIB",
    "tnRmdSystemId")

(tnRmdMIBModules,
 tnRmdObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnRmdMIBModules",
    "tnRmdObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnRmdCfmMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tnRmdCfmMibModule.setRevisions(
        ("2012-11-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TnRmdCfmMegId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(48, 48),
    )
    fixed_length = 48



class TnRmdCfmMepDefect(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("unl", 0),
          ("mmg", 1),
          ("unm", 2),
          ("loc", 3),
          ("rdi", 4),
          ("unp", 5))
    )


class TnRmdCfmMepNumber(TextualConvention, Unsigned32):
    status = "current"


class TnRmdCfmMeasurementInterval(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3600000),
    )



# MIB Managed Objects in the order of their OIDs

_TnRmdCfmObjects_ObjectIdentity = ObjectIdentity
tnRmdCfmObjects = _TnRmdCfmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1)
)
_TnRmdCfmAttributeTotal_Type = Integer32
_TnRmdCfmAttributeTotal_Object = MibScalar
tnRmdCfmAttributeTotal = _TnRmdCfmAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 1),
    _TnRmdCfmAttributeTotal_Type()
)
tnRmdCfmAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdCfmAttributeTotal.setStatus("current")
_TnRmdSystemCfmTable_Object = MibTable
tnRmdSystemCfmTable = _TnRmdSystemCfmTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnRmdSystemCfmTable.setStatus("current")
_TnRmdSystemCfmEntry_Object = MibTableRow
tnRmdSystemCfmEntry = _TnRmdSystemCfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 2, 1)
)
tnRmdSystemCfmEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
)
if mibBuilder.loadTexts:
    tnRmdSystemCfmEntry.setStatus("current")
_TnRmdSystemCfmMaxNrMeps_Type = Unsigned32
_TnRmdSystemCfmMaxNrMeps_Object = MibTableColumn
tnRmdSystemCfmMaxNrMeps = _TnRmdSystemCfmMaxNrMeps_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 2, 1, 1),
    _TnRmdSystemCfmMaxNrMeps_Type()
)
tnRmdSystemCfmMaxNrMeps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemCfmMaxNrMeps.setStatus("current")
_TnRmdSystemCfmLmMaxNrPriorityLevels_Type = Unsigned32
_TnRmdSystemCfmLmMaxNrPriorityLevels_Object = MibTableColumn
tnRmdSystemCfmLmMaxNrPriorityLevels = _TnRmdSystemCfmLmMaxNrPriorityLevels_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 2, 1, 2),
    _TnRmdSystemCfmLmMaxNrPriorityLevels_Type()
)
tnRmdSystemCfmLmMaxNrPriorityLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdSystemCfmLmMaxNrPriorityLevels.setStatus("current")
_TnRmdSystemCfmDmUpdateLocalTime_Type = TruthValue
_TnRmdSystemCfmDmUpdateLocalTime_Object = MibTableColumn
tnRmdSystemCfmDmUpdateLocalTime = _TnRmdSystemCfmDmUpdateLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 2, 1, 3),
    _TnRmdSystemCfmDmUpdateLocalTime_Type()
)
tnRmdSystemCfmDmUpdateLocalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnRmdSystemCfmDmUpdateLocalTime.setStatus("current")
_TnRmdCfmMepTable_Object = MibTable
tnRmdCfmMepTable = _TnRmdCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnRmdCfmMepTable.setStatus("current")
_TnRmdCfmMepEntry_Object = MibTableRow
tnRmdCfmMepEntry = _TnRmdCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1)
)
tnRmdCfmMepEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
    (0, "TN-RMD-CFM-MIB", "tnRmdCfmMepNumber"),
)
if mibBuilder.loadTexts:
    tnRmdCfmMepEntry.setStatus("current")
_TnRmdCfmMepNumber_Type = TnRmdCfmMepNumber
_TnRmdCfmMepNumber_Object = MibTableColumn
tnRmdCfmMepNumber = _TnRmdCfmMepNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 1),
    _TnRmdCfmMepNumber_Type()
)
tnRmdCfmMepNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdCfmMepNumber.setStatus("current")
_TnRmdCfmMepMdIndex_Type = Unsigned32
_TnRmdCfmMepMdIndex_Object = MibTableColumn
tnRmdCfmMepMdIndex = _TnRmdCfmMepMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 2),
    _TnRmdCfmMepMdIndex_Type()
)
tnRmdCfmMepMdIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepMdIndex.setStatus("current")


class _TnRmdCfmMepMdFormat_Type(Dot1agCfmMaintDomainNameType):
    """Custom type tnRmdCfmMepMdFormat based on Dot1agCfmMaintDomainNameType"""
    defaultValue = 4


_TnRmdCfmMepMdFormat_Type.__name__ = "Dot1agCfmMaintDomainNameType"
_TnRmdCfmMepMdFormat_Object = MibTableColumn
tnRmdCfmMepMdFormat = _TnRmdCfmMepMdFormat_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 3),
    _TnRmdCfmMepMdFormat_Type()
)
tnRmdCfmMepMdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepMdFormat.setStatus("current")


class _TnRmdCfmMepMdName_Type(Dot1agCfmMaintDomainName):
    """Custom type tnRmdCfmMepMdName based on Dot1agCfmMaintDomainName"""
    defaultValue = OctetString("DEFAULT")


_TnRmdCfmMepMdName_Type.__name__ = "Dot1agCfmMaintDomainName"
_TnRmdCfmMepMdName_Object = MibTableColumn
tnRmdCfmMepMdName = _TnRmdCfmMepMdName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 4),
    _TnRmdCfmMepMdName_Type()
)
tnRmdCfmMepMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepMdName.setStatus("current")
_TnRmdCfmMepMaIndex_Type = Unsigned32
_TnRmdCfmMepMaIndex_Object = MibTableColumn
tnRmdCfmMepMaIndex = _TnRmdCfmMepMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 5),
    _TnRmdCfmMepMaIndex_Type()
)
tnRmdCfmMepMaIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepMaIndex.setStatus("current")
_TnRmdCfmMepMaNetFormat_Type = Dot1agCfmMaintAssocNameType
_TnRmdCfmMepMaNetFormat_Object = MibTableColumn
tnRmdCfmMepMaNetFormat = _TnRmdCfmMepMaNetFormat_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 6),
    _TnRmdCfmMepMaNetFormat_Type()
)
tnRmdCfmMepMaNetFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepMaNetFormat.setStatus("current")
_TnRmdCfmMepMaNetName_Type = Dot1agCfmMaintAssocName
_TnRmdCfmMepMaNetName_Object = MibTableColumn
tnRmdCfmMepMaNetName = _TnRmdCfmMepMaNetName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 7),
    _TnRmdCfmMepMaNetName_Type()
)
tnRmdCfmMepMaNetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepMaNetName.setStatus("current")
_TnRmdCfmMepMdLevel_Type = Dot1agCfmMDLevel
_TnRmdCfmMepMdLevel_Object = MibTableColumn
tnRmdCfmMepMdLevel = _TnRmdCfmMepMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 8),
    _TnRmdCfmMepMdLevel_Type()
)
tnRmdCfmMepMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepMdLevel.setStatus("current")
_TnRmdCfmMepMegId_Type = TnRmdCfmMegId
_TnRmdCfmMepMegId_Object = MibTableColumn
tnRmdCfmMepMegId = _TnRmdCfmMepMegId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 9),
    _TnRmdCfmMepMegId_Type()
)
tnRmdCfmMepMegId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepMegId.setStatus("current")
_TnRmdCfmMepDirection_Type = Dot1agCfmMpDirection
_TnRmdCfmMepDirection_Object = MibTableColumn
tnRmdCfmMepDirection = _TnRmdCfmMepDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 10),
    _TnRmdCfmMepDirection_Type()
)
tnRmdCfmMepDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdCfmMepDirection.setStatus("current")
_TnRmdCfmMepLocalId_Type = Dot1agCfmMepId
_TnRmdCfmMepLocalId_Object = MibTableColumn
tnRmdCfmMepLocalId = _TnRmdCfmMepLocalId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 11),
    _TnRmdCfmMepLocalId_Type()
)
tnRmdCfmMepLocalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepLocalId.setStatus("current")
_TnRmdCfmMepEnabled_Type = TruthValue
_TnRmdCfmMepEnabled_Object = MibTableColumn
tnRmdCfmMepEnabled = _TnRmdCfmMepEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 12),
    _TnRmdCfmMepEnabled_Type()
)
tnRmdCfmMepEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepEnabled.setStatus("current")
_TnRmdCfmMepCcmEnabled_Type = TruthValue
_TnRmdCfmMepCcmEnabled_Object = MibTableColumn
tnRmdCfmMepCcmEnabled = _TnRmdCfmMepCcmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 13),
    _TnRmdCfmMepCcmEnabled_Type()
)
tnRmdCfmMepCcmEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepCcmEnabled.setStatus("current")
_TnRmdCfmMepLbrEnabled_Type = TruthValue
_TnRmdCfmMepLbrEnabled_Object = MibTableColumn
tnRmdCfmMepLbrEnabled = _TnRmdCfmMepLbrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 14),
    _TnRmdCfmMepLbrEnabled_Type()
)
tnRmdCfmMepLbrEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepLbrEnabled.setStatus("current")
_TnRmdCfmMepCcmInterval_Type = Dot1agCfmCcmInterval
_TnRmdCfmMepCcmInterval_Object = MibTableColumn
tnRmdCfmMepCcmInterval = _TnRmdCfmMepCcmInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 15),
    _TnRmdCfmMepCcmInterval_Type()
)
tnRmdCfmMepCcmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepCcmInterval.setStatus("current")
_TnRmdCfmMepIfIndex_Type = InterfaceIndexOrZero
_TnRmdCfmMepIfIndex_Object = MibTableColumn
tnRmdCfmMepIfIndex = _TnRmdCfmMepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 16),
    _TnRmdCfmMepIfIndex_Type()
)
tnRmdCfmMepIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepIfIndex.setStatus("current")
_TnRmdCfmMepVlanId_Type = VlanIdOrNone
_TnRmdCfmMepVlanId_Object = MibTableColumn
tnRmdCfmMepVlanId = _TnRmdCfmMepVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 17),
    _TnRmdCfmMepVlanId_Type()
)
tnRmdCfmMepVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepVlanId.setStatus("current")
_TnRmdCfmMepDefect_Type = TnRmdCfmMepDefect
_TnRmdCfmMepDefect_Object = MibTableColumn
tnRmdCfmMepDefect = _TnRmdCfmMepDefect_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 18),
    _TnRmdCfmMepDefect_Type()
)
tnRmdCfmMepDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRmdCfmMepDefect.setStatus("current")
_TnRmdCfmMepRowStatus_Type = RowStatus
_TnRmdCfmMepRowStatus_Object = MibTableColumn
tnRmdCfmMepRowStatus = _TnRmdCfmMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 3, 1, 19),
    _TnRmdCfmMepRowStatus_Type()
)
tnRmdCfmMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmMepRowStatus.setStatus("current")
_TnRmdCfmRemoteMepTable_Object = MibTable
tnRmdCfmRemoteMepTable = _TnRmdCfmRemoteMepTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tnRmdCfmRemoteMepTable.setStatus("current")
_TnRmdCfmRemoteMepEntry_Object = MibTableRow
tnRmdCfmRemoteMepEntry = _TnRmdCfmRemoteMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 4, 1)
)
tnRmdCfmRemoteMepEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-RMD-SYSTEM-MIB", "tnRmdSystemId"),
    (0, "TN-RMD-CFM-MIB", "tnRmdCfmMepNumber"),
    (0, "TN-RMD-CFM-MIB", "tnRmdCfmRemoteMepId"),
)
if mibBuilder.loadTexts:
    tnRmdCfmRemoteMepEntry.setStatus("current")
_TnRmdCfmRemoteMepId_Type = Dot1agCfmMepId
_TnRmdCfmRemoteMepId_Object = MibTableColumn
tnRmdCfmRemoteMepId = _TnRmdCfmRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 4, 1, 1),
    _TnRmdCfmRemoteMepId_Type()
)
tnRmdCfmRemoteMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnRmdCfmRemoteMepId.setStatus("current")
_TnRmdCfmRemoteMepRowStatus_Type = RowStatus
_TnRmdCfmRemoteMepRowStatus_Object = MibTableColumn
tnRmdCfmRemoteMepRowStatus = _TnRmdCfmRemoteMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 4, 1, 1, 4, 1, 2),
    _TnRmdCfmRemoteMepRowStatus_Type()
)
tnRmdCfmRemoteMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnRmdCfmRemoteMepRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-RMD-CFM-MIB",
    **{"TnRmdCfmMegId": TnRmdCfmMegId,
       "TnRmdCfmMepDefect": TnRmdCfmMepDefect,
       "TnRmdCfmMepNumber": TnRmdCfmMepNumber,
       "TnRmdCfmMeasurementInterval": TnRmdCfmMeasurementInterval,
       "tnRmdCfmMibModule": tnRmdCfmMibModule,
       "tnRmdCfmObjects": tnRmdCfmObjects,
       "tnRmdCfmAttributeTotal": tnRmdCfmAttributeTotal,
       "tnRmdSystemCfmTable": tnRmdSystemCfmTable,
       "tnRmdSystemCfmEntry": tnRmdSystemCfmEntry,
       "tnRmdSystemCfmMaxNrMeps": tnRmdSystemCfmMaxNrMeps,
       "tnRmdSystemCfmLmMaxNrPriorityLevels": tnRmdSystemCfmLmMaxNrPriorityLevels,
       "tnRmdSystemCfmDmUpdateLocalTime": tnRmdSystemCfmDmUpdateLocalTime,
       "tnRmdCfmMepTable": tnRmdCfmMepTable,
       "tnRmdCfmMepEntry": tnRmdCfmMepEntry,
       "tnRmdCfmMepNumber": tnRmdCfmMepNumber,
       "tnRmdCfmMepMdIndex": tnRmdCfmMepMdIndex,
       "tnRmdCfmMepMdFormat": tnRmdCfmMepMdFormat,
       "tnRmdCfmMepMdName": tnRmdCfmMepMdName,
       "tnRmdCfmMepMaIndex": tnRmdCfmMepMaIndex,
       "tnRmdCfmMepMaNetFormat": tnRmdCfmMepMaNetFormat,
       "tnRmdCfmMepMaNetName": tnRmdCfmMepMaNetName,
       "tnRmdCfmMepMdLevel": tnRmdCfmMepMdLevel,
       "tnRmdCfmMepMegId": tnRmdCfmMepMegId,
       "tnRmdCfmMepDirection": tnRmdCfmMepDirection,
       "tnRmdCfmMepLocalId": tnRmdCfmMepLocalId,
       "tnRmdCfmMepEnabled": tnRmdCfmMepEnabled,
       "tnRmdCfmMepCcmEnabled": tnRmdCfmMepCcmEnabled,
       "tnRmdCfmMepLbrEnabled": tnRmdCfmMepLbrEnabled,
       "tnRmdCfmMepCcmInterval": tnRmdCfmMepCcmInterval,
       "tnRmdCfmMepIfIndex": tnRmdCfmMepIfIndex,
       "tnRmdCfmMepVlanId": tnRmdCfmMepVlanId,
       "tnRmdCfmMepDefect": tnRmdCfmMepDefect,
       "tnRmdCfmMepRowStatus": tnRmdCfmMepRowStatus,
       "tnRmdCfmRemoteMepTable": tnRmdCfmRemoteMepTable,
       "tnRmdCfmRemoteMepEntry": tnRmdCfmRemoteMepEntry,
       "tnRmdCfmRemoteMepId": tnRmdCfmRemoteMepId,
       "tnRmdCfmRemoteMepRowStatus": tnRmdCfmRemoteMepRowStatus}
)
