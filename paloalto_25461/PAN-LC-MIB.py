# SNMP MIB module (PAN-LC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/paloalto_25461/PAN-LC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:51:51 2025
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

(panModules,
 panProductsMibs) = mibBuilder.importSymbols(
    "PAN-GLOBAL-REG",
    "panModules",
    "panProductsMibs")

(panM_100,) = mibBuilder.importSymbols(
    "PAN-PRODUCTS-MIB",
    "panM-100")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

panLogCollectorMibsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 6)
)
if mibBuilder.loadTexts:
    panLogCollectorMibsModule.setRevisions(
        ("2012-01-11 10:13",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PanLcStat_ObjectIdentity = ObjectIdentity
panLcStat = _PanLcStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1)
)
if mibBuilder.loadTexts:
    panLcStat.setStatus("current")
_PanLcLogRate_Type = Unsigned32
_PanLcLogRate_Object = MibScalar
panLcLogRate = _PanLcLogRate_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 1),
    _PanLcLogRate_Type()
)
panLcLogRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogRate.setStatus("current")
_PanLcLogDuration_ObjectIdentity = ObjectIdentity
panLcLogDuration = _PanLcLogDuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2)
)
if mibBuilder.loadTexts:
    panLcLogDuration.setStatus("current")
_PanLcLogDurationTraffic_Type = Unsigned32
_PanLcLogDurationTraffic_Object = MibScalar
panLcLogDurationTraffic = _PanLcLogDurationTraffic_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 1),
    _PanLcLogDurationTraffic_Type()
)
panLcLogDurationTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationTraffic.setStatus("current")
_PanLcLogDurationConfig_Type = Unsigned32
_PanLcLogDurationConfig_Object = MibScalar
panLcLogDurationConfig = _PanLcLogDurationConfig_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 2),
    _PanLcLogDurationConfig_Type()
)
panLcLogDurationConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationConfig.setStatus("current")
_PanLcLogDurationSystem_Type = Unsigned32
_PanLcLogDurationSystem_Object = MibScalar
panLcLogDurationSystem = _PanLcLogDurationSystem_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 3),
    _PanLcLogDurationSystem_Type()
)
panLcLogDurationSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationSystem.setStatus("current")
_PanLcLogDurationThreat_Type = Unsigned32
_PanLcLogDurationThreat_Object = MibScalar
panLcLogDurationThreat = _PanLcLogDurationThreat_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 4),
    _PanLcLogDurationThreat_Type()
)
panLcLogDurationThreat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationThreat.setStatus("current")
_PanLcLogDurationAppstat_Type = Unsigned32
_PanLcLogDurationAppstat_Object = MibScalar
panLcLogDurationAppstat = _PanLcLogDurationAppstat_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 5),
    _PanLcLogDurationAppstat_Type()
)
panLcLogDurationAppstat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationAppstat.setStatus("current")
_PanLcLogDurationTrsum_Type = Unsigned32
_PanLcLogDurationTrsum_Object = MibScalar
panLcLogDurationTrsum = _PanLcLogDurationTrsum_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 6),
    _PanLcLogDurationTrsum_Type()
)
panLcLogDurationTrsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationTrsum.setStatus("current")
_PanLcLogDurationThsum_Type = Unsigned32
_PanLcLogDurationThsum_Object = MibScalar
panLcLogDurationThsum = _PanLcLogDurationThsum_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 7),
    _PanLcLogDurationThsum_Type()
)
panLcLogDurationThsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationThsum.setStatus("current")
_PanLcLogDurationEvent_Type = Unsigned32
_PanLcLogDurationEvent_Object = MibScalar
panLcLogDurationEvent = _PanLcLogDurationEvent_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 8),
    _PanLcLogDurationEvent_Type()
)
panLcLogDurationEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationEvent.setStatus("current")
_PanLcLogDurationAlarm_Type = Unsigned32
_PanLcLogDurationAlarm_Object = MibScalar
panLcLogDurationAlarm = _PanLcLogDurationAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 9),
    _PanLcLogDurationAlarm_Type()
)
panLcLogDurationAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationAlarm.setStatus("current")
_PanLcLogDurationHipmatch_Type = Unsigned32
_PanLcLogDurationHipmatch_Object = MibScalar
panLcLogDurationHipmatch = _PanLcLogDurationHipmatch_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 10),
    _PanLcLogDurationHipmatch_Type()
)
panLcLogDurationHipmatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationHipmatch.setStatus("current")
_PanLcLogDurationUserid_Type = Unsigned32
_PanLcLogDurationUserid_Object = MibScalar
panLcLogDurationUserid = _PanLcLogDurationUserid_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 2, 11),
    _PanLcLogDurationUserid_Type()
)
panLcLogDurationUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationUserid.setStatus("current")
_PanLcDiskUsage_ObjectIdentity = ObjectIdentity
panLcDiskUsage = _PanLcDiskUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3)
)
if mibBuilder.loadTexts:
    panLcDiskUsage.setStatus("current")
_PanLcDiskUsageLd1_Type = Unsigned32
_PanLcDiskUsageLd1_Object = MibScalar
panLcDiskUsageLd1 = _PanLcDiskUsageLd1_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3, 1),
    _PanLcDiskUsageLd1_Type()
)
panLcDiskUsageLd1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcDiskUsageLd1.setStatus("current")
_PanLcDiskUsageLd2_Type = Unsigned32
_PanLcDiskUsageLd2_Object = MibScalar
panLcDiskUsageLd2 = _PanLcDiskUsageLd2_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3, 2),
    _PanLcDiskUsageLd2_Type()
)
panLcDiskUsageLd2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcDiskUsageLd2.setStatus("current")
_PanLcDiskUsageLd3_Type = Unsigned32
_PanLcDiskUsageLd3_Object = MibScalar
panLcDiskUsageLd3 = _PanLcDiskUsageLd3_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3, 3),
    _PanLcDiskUsageLd3_Type()
)
panLcDiskUsageLd3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcDiskUsageLd3.setStatus("current")
_PanLcDiskUsageLd4_Type = Unsigned32
_PanLcDiskUsageLd4_Object = MibScalar
panLcDiskUsageLd4 = _PanLcDiskUsageLd4_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 1, 3, 4),
    _PanLcDiskUsageLd4_Type()
)
panLcDiskUsageLd4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcDiskUsageLd4.setStatus("current")
_PanLcIsRedundancyMember_Type = TruthValue
_PanLcIsRedundancyMember_Object = MibScalar
panLcIsRedundancyMember = _PanLcIsRedundancyMember_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 3, 30, 2),
    _PanLcIsRedundancyMember_Type()
)
panLcIsRedundancyMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcIsRedundancyMember.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAN-LC-MIB",
    **{"panLogCollectorMibsModule": panLogCollectorMibsModule,
       "panLcStat": panLcStat,
       "panLcLogRate": panLcLogRate,
       "panLcLogDuration": panLcLogDuration,
       "panLcLogDurationTraffic": panLcLogDurationTraffic,
       "panLcLogDurationConfig": panLcLogDurationConfig,
       "panLcLogDurationSystem": panLcLogDurationSystem,
       "panLcLogDurationThreat": panLcLogDurationThreat,
       "panLcLogDurationAppstat": panLcLogDurationAppstat,
       "panLcLogDurationTrsum": panLcLogDurationTrsum,
       "panLcLogDurationThsum": panLcLogDurationThsum,
       "panLcLogDurationEvent": panLcLogDurationEvent,
       "panLcLogDurationAlarm": panLcLogDurationAlarm,
       "panLcLogDurationHipmatch": panLcLogDurationHipmatch,
       "panLcLogDurationUserid": panLcLogDurationUserid,
       "panLcDiskUsage": panLcDiskUsage,
       "panLcDiskUsageLd1": panLcDiskUsageLd1,
       "panLcDiskUsageLd2": panLcDiskUsageLd2,
       "panLcDiskUsageLd3": panLcDiskUsageLd3,
       "panLcDiskUsageLd4": panLcDiskUsageLd4,
       "panLcIsRedundancyMember": panLcIsRedundancyMember}
)
