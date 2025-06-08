# SNMP MIB module (RUIJIE-MPLS-SIGNAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-MPLS-SIGNAL-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:12 2025
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(AreaID,
 DesignatedRouterPriority,
 HelloRange,
 PositiveInteger,
 RouterID,
 Status) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "DesignatedRouterPriority",
    "HelloRange",
    "PositiveInteger",
    "RouterID",
    "Status")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ruijieMplsSignalMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98)
)
if mibBuilder.loadTexts:
    ruijieMplsSignalMIB.setRevisions(
        ("2011-05-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieMplsSignalMIBObjects_ObjectIdentity = ObjectIdentity
ruijieMplsSignalMIBObjects = _RuijieMplsSignalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1)
)
_RuijieMplsSignalObjects_ObjectIdentity = ObjectIdentity
ruijieMplsSignalObjects = _RuijieMplsSignalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1)
)
_RuijieMplsSignalmplsGernalMibObjects_ObjectIdentity = ObjectIdentity
ruijieMplsSignalmplsGernalMibObjects = _RuijieMplsSignalmplsGernalMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 1)
)
_RuijieMplsVersion_Type = Unsigned32
_RuijieMplsVersion_Object = MibScalar
ruijieMplsVersion = _RuijieMplsVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 1, 1),
    _RuijieMplsVersion_Type()
)
ruijieMplsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMplsVersion.setStatus("current")


class _RuijieMPLSSignal_Type(Integer32):
    """Custom type ruijieMPLSSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ldp", 1),
          ("rsvp-te", 2),
          ("cr-ldp", 3),
          ("other", 4))
    )


_RuijieMPLSSignal_Type.__name__ = "Integer32"
_RuijieMPLSSignal_Object = MibScalar
ruijieMPLSSignal = _RuijieMPLSSignal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 1, 2),
    _RuijieMPLSSignal_Type()
)
ruijieMPLSSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSSignal.setStatus("current")
_RuijieMPLSTESignal_Type = TruthValue
_RuijieMPLSTESignal_Object = MibScalar
ruijieMPLSTESignal = _RuijieMPLSTESignal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 1, 3),
    _RuijieMPLSTESignal_Type()
)
ruijieMPLSTESignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSTESignal.setStatus("current")
_RuijieMplsSignalConfigMibObjects_ObjectIdentity = ObjectIdentity
ruijieMplsSignalConfigMibObjects = _RuijieMplsSignalConfigMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 2)
)
_RuijieMPLSConfigLspNum_Type = Unsigned32
_RuijieMPLSConfigLspNum_Object = MibScalar
ruijieMPLSConfigLspNum = _RuijieMPLSConfigLspNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 2, 1),
    _RuijieMPLSConfigLspNum_Type()
)
ruijieMPLSConfigLspNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSConfigLspNum.setStatus("current")
_RuijieMPLSActiveLspNum_Type = Unsigned32
_RuijieMPLSActiveLspNum_Object = MibScalar
ruijieMPLSActiveLspNum = _RuijieMPLSActiveLspNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 2, 2),
    _RuijieMPLSActiveLspNum_Type()
)
ruijieMPLSActiveLspNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSActiveLspNum.setStatus("current")
_RuijieMPLSAdministrativeGroupTable_Object = MibTable
ruijieMPLSAdministrativeGroupTable = _RuijieMPLSAdministrativeGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieMPLSAdministrativeGroupTable.setStatus("current")
_RuijieMPLSAdministrativeGroupEntry_Object = MibTableRow
ruijieMPLSAdministrativeGroupEntry = _RuijieMPLSAdministrativeGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1)
)
ruijieMPLSAdministrativeGroupEntry.setIndexNames(
    (0, "RUIJIE-MPLS-SIGNAL-MIB", "ruijieMPLSFecIndex"),
)
if mibBuilder.loadTexts:
    ruijieMPLSAdministrativeGroupEntry.setStatus("current")
_RuijieMPLSFecIndex_Type = Integer32
_RuijieMPLSFecIndex_Object = MibTableColumn
ruijieMPLSFecIndex = _RuijieMPLSFecIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1, 1),
    _RuijieMPLSFecIndex_Type()
)
ruijieMPLSFecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieMPLSFecIndex.setStatus("current")
_RuijieMPLSLSPName_Type = DisplayString
_RuijieMPLSLSPName_Object = MibTableColumn
ruijieMPLSLSPName = _RuijieMPLSLSPName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1, 2),
    _RuijieMPLSLSPName_Type()
)
ruijieMPLSLSPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSLSPName.setStatus("current")


class _RuijieMPLSLSPStates_Type(Integer32):
    """Custom type ruijieMPLSLSPStates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RuijieMPLSLSPStates_Type.__name__ = "Integer32"
_RuijieMPLSLSPStates_Object = MibTableColumn
ruijieMPLSLSPStates = _RuijieMPLSLSPStates_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1, 3),
    _RuijieMPLSLSPStates_Type()
)
ruijieMPLSLSPStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSLSPStates.setStatus("current")
_RuijieMPLSLSPForwardBytes_Type = Integer32
_RuijieMPLSLSPForwardBytes_Object = MibTableColumn
ruijieMPLSLSPForwardBytes = _RuijieMPLSLSPForwardBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1, 4),
    _RuijieMPLSLSPForwardBytes_Type()
)
ruijieMPLSLSPForwardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSLSPForwardBytes.setStatus("current")
_RuijieMPLSLSPForwardPackets_Type = Integer32
_RuijieMPLSLSPForwardPackets_Object = MibTableColumn
ruijieMPLSLSPForwardPackets = _RuijieMPLSLSPForwardPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1, 5),
    _RuijieMPLSLSPForwardPackets_Type()
)
ruijieMPLSLSPForwardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSLSPForwardPackets.setStatus("current")
_RuijieMPLSLSPActiveTime_Type = TimeStamp
_RuijieMPLSLSPActiveTime_Object = MibTableColumn
ruijieMPLSLSPActiveTime = _RuijieMPLSLSPActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1, 6),
    _RuijieMPLSLSPActiveTime_Type()
)
ruijieMPLSLSPActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSLSPActiveTime.setStatus("current")
_RuijieMPLSLSPCreationTime_Type = TimeStamp
_RuijieMPLSLSPCreationTime_Object = MibTableColumn
ruijieMPLSLSPCreationTime = _RuijieMPLSLSPCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1, 7),
    _RuijieMPLSLSPCreationTime_Type()
)
ruijieMPLSLSPCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSLSPCreationTime.setStatus("current")
_RuijieMPLSLSPPrimaryCreationTime_Type = TimeStamp
_RuijieMPLSLSPPrimaryCreationTime_Object = MibTableColumn
ruijieMPLSLSPPrimaryCreationTime = _RuijieMPLSLSPPrimaryCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1, 8),
    _RuijieMPLSLSPPrimaryCreationTime_Type()
)
ruijieMPLSLSPPrimaryCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSLSPPrimaryCreationTime.setStatus("current")
_RuijieMPLSLSPSwitchTimes_Type = Integer32
_RuijieMPLSLSPSwitchTimes_Object = MibTableColumn
ruijieMPLSLSPSwitchTimes = _RuijieMPLSLSPSwitchTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1, 9),
    _RuijieMPLSLSPSwitchTimes_Type()
)
ruijieMPLSLSPSwitchTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSLSPSwitchTimes.setStatus("current")
_RuijieMPLSLSPLatestSwitchTime_Type = TimeStamp
_RuijieMPLSLSPLatestSwitchTime_Object = MibTableColumn
ruijieMPLSLSPLatestSwitchTime = _RuijieMPLSLSPLatestSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1, 10),
    _RuijieMPLSLSPLatestSwitchTime_Type()
)
ruijieMPLSLSPLatestSwitchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSLSPLatestSwitchTime.setStatus("current")
_RuijieMPLSLSPPathchangeTime_Type = TimeStamp
_RuijieMPLSLSPPathchangeTime_Object = MibTableColumn
ruijieMPLSLSPPathchangeTime = _RuijieMPLSLSPPathchangeTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1, 11),
    _RuijieMPLSLSPPathchangeTime_Type()
)
ruijieMPLSLSPPathchangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSLSPPathchangeTime.setStatus("current")
_RuijieMPLSLSPConfigChangeTime_Type = TimeStamp
_RuijieMPLSLSPConfigChangeTime_Object = MibTableColumn
ruijieMPLSLSPConfigChangeTime = _RuijieMPLSLSPConfigChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1, 12),
    _RuijieMPLSLSPConfigChangeTime_Type()
)
ruijieMPLSLSPConfigChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSLSPConfigChangeTime.setStatus("current")
_RuijieMPLSLSPBackupPath_Type = DisplayString
_RuijieMPLSLSPBackupPath_Object = MibTableColumn
ruijieMPLSLSPBackupPath = _RuijieMPLSLSPBackupPath_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1, 13),
    _RuijieMPLSLSPBackupPath_Type()
)
ruijieMPLSLSPBackupPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSLSPBackupPath.setStatus("current")


class _RuijieMPLSLSPOperationPath_Type(Integer32):
    """Custom type ruijieMPLSLSPOperationPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2),
          ("none", 3))
    )


_RuijieMPLSLSPOperationPath_Type.__name__ = "Integer32"
_RuijieMPLSLSPOperationPath_Object = MibTableColumn
ruijieMPLSLSPOperationPath = _RuijieMPLSLSPOperationPath_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1, 14),
    _RuijieMPLSLSPOperationPath_Type()
)
ruijieMPLSLSPOperationPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSLSPOperationPath.setStatus("current")
_RuijieMPLSLSPIngress_Type = InetAddressType
_RuijieMPLSLSPIngress_Object = MibTableColumn
ruijieMPLSLSPIngress = _RuijieMPLSLSPIngress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1, 15),
    _RuijieMPLSLSPIngress_Type()
)
ruijieMPLSLSPIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSLSPIngress.setStatus("current")
_RuijieMPLSLSPDestination_Type = InetAddressType
_RuijieMPLSLSPDestination_Object = MibTableColumn
ruijieMPLSLSPDestination = _RuijieMPLSLSPDestination_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1, 16),
    _RuijieMPLSLSPDestination_Type()
)
ruijieMPLSLSPDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSLSPDestination.setStatus("current")
_RuijieMPLSLSPAdministrativeGroupName_Type = DisplayString
_RuijieMPLSLSPAdministrativeGroupName_Object = MibTableColumn
ruijieMPLSLSPAdministrativeGroupName = _RuijieMPLSLSPAdministrativeGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 1, 3, 1, 17),
    _RuijieMPLSLSPAdministrativeGroupName_Type()
)
ruijieMPLSLSPAdministrativeGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMPLSLSPAdministrativeGroupName.setStatus("current")
_RuijieMplsSignalConformance_ObjectIdentity = ObjectIdentity
ruijieMplsSignalConformance = _RuijieMplsSignalConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 98, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-MPLS-SIGNAL-MIB",
    **{"ruijieMplsSignalMIB": ruijieMplsSignalMIB,
       "ruijieMplsSignalMIBObjects": ruijieMplsSignalMIBObjects,
       "ruijieMplsSignalObjects": ruijieMplsSignalObjects,
       "ruijieMplsSignalmplsGernalMibObjects": ruijieMplsSignalmplsGernalMibObjects,
       "ruijieMplsVersion": ruijieMplsVersion,
       "ruijieMPLSSignal": ruijieMPLSSignal,
       "ruijieMPLSTESignal": ruijieMPLSTESignal,
       "ruijieMplsSignalConfigMibObjects": ruijieMplsSignalConfigMibObjects,
       "ruijieMPLSConfigLspNum": ruijieMPLSConfigLspNum,
       "ruijieMPLSActiveLspNum": ruijieMPLSActiveLspNum,
       "ruijieMPLSAdministrativeGroupTable": ruijieMPLSAdministrativeGroupTable,
       "ruijieMPLSAdministrativeGroupEntry": ruijieMPLSAdministrativeGroupEntry,
       "ruijieMPLSFecIndex": ruijieMPLSFecIndex,
       "ruijieMPLSLSPName": ruijieMPLSLSPName,
       "ruijieMPLSLSPStates": ruijieMPLSLSPStates,
       "ruijieMPLSLSPForwardBytes": ruijieMPLSLSPForwardBytes,
       "ruijieMPLSLSPForwardPackets": ruijieMPLSLSPForwardPackets,
       "ruijieMPLSLSPActiveTime": ruijieMPLSLSPActiveTime,
       "ruijieMPLSLSPCreationTime": ruijieMPLSLSPCreationTime,
       "ruijieMPLSLSPPrimaryCreationTime": ruijieMPLSLSPPrimaryCreationTime,
       "ruijieMPLSLSPSwitchTimes": ruijieMPLSLSPSwitchTimes,
       "ruijieMPLSLSPLatestSwitchTime": ruijieMPLSLSPLatestSwitchTime,
       "ruijieMPLSLSPPathchangeTime": ruijieMPLSLSPPathchangeTime,
       "ruijieMPLSLSPConfigChangeTime": ruijieMPLSLSPConfigChangeTime,
       "ruijieMPLSLSPBackupPath": ruijieMPLSLSPBackupPath,
       "ruijieMPLSLSPOperationPath": ruijieMPLSLSPOperationPath,
       "ruijieMPLSLSPIngress": ruijieMPLSLSPIngress,
       "ruijieMPLSLSPDestination": ruijieMPLSLSPDestination,
       "ruijieMPLSLSPAdministrativeGroupName": ruijieMPLSLSPAdministrativeGroupName,
       "ruijieMplsSignalConformance": ruijieMplsSignalConformance}
)
