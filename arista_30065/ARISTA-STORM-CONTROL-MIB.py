# SNMP MIB module (ARISTA-STORM-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-STORM-CONTROL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:36 2025
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

aristaStormControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 35)
)
if mibBuilder.loadTexts:
    aristaStormControlMIB.setRevisions(
        ("2024-12-19 00:00",
         "2023-07-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AristaStormControlTrafficClass(TextualConvention, Integer32):
    status = "current"
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
        *(("all", 0),
          ("broadcast", 1),
          ("multicast", 2),
          ("unknownUnicast", 3),
          ("allUnicast", 4))
    )



class AristaStormControlThresholdUnits(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("percent", 0),
          ("pps", 1),
          ("bps", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AristaStormControlMibNotifications_ObjectIdentity = ObjectIdentity
aristaStormControlMibNotifications = _AristaStormControlMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 35, 0)
)
_AristaStormControlMibObjects_ObjectIdentity = ObjectIdentity
aristaStormControlMibObjects = _AristaStormControlMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 35, 1)
)
_AristaStormControlIfTable_Object = MibTable
aristaStormControlIfTable = _AristaStormControlIfTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 35, 1, 1)
)
if mibBuilder.loadTexts:
    aristaStormControlIfTable.setStatus("current")
_AristaStormControlIfEntry_Object = MibTableRow
aristaStormControlIfEntry = _AristaStormControlIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 35, 1, 1, 1)
)
aristaStormControlIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARISTA-STORM-CONTROL-MIB", "aristaStormControlIfTrafficClass"),
)
if mibBuilder.loadTexts:
    aristaStormControlIfEntry.setStatus("current")
_AristaStormControlIfTrafficClass_Type = AristaStormControlTrafficClass
_AristaStormControlIfTrafficClass_Object = MibTableColumn
aristaStormControlIfTrafficClass = _AristaStormControlIfTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 35, 1, 1, 1, 1),
    _AristaStormControlIfTrafficClass_Type()
)
aristaStormControlIfTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaStormControlIfTrafficClass.setStatus("current")
_AristaStormControlIfThresholdLevel_Type = CounterBasedGauge64
_AristaStormControlIfThresholdLevel_Object = MibTableColumn
aristaStormControlIfThresholdLevel = _AristaStormControlIfThresholdLevel_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 35, 1, 1, 1, 2),
    _AristaStormControlIfThresholdLevel_Type()
)
aristaStormControlIfThresholdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaStormControlIfThresholdLevel.setStatus("current")
_AristaStormControlIfThresholdUnits_Type = AristaStormControlThresholdUnits
_AristaStormControlIfThresholdUnits_Object = MibTableColumn
aristaStormControlIfThresholdUnits = _AristaStormControlIfThresholdUnits_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 35, 1, 1, 1, 3),
    _AristaStormControlIfThresholdUnits_Type()
)
aristaStormControlIfThresholdUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaStormControlIfThresholdUnits.setStatus("current")
_AristaStormControlIfDrops_Type = Counter64
_AristaStormControlIfDrops_Object = MibTableColumn
aristaStormControlIfDrops = _AristaStormControlIfDrops_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 35, 1, 1, 1, 4),
    _AristaStormControlIfDrops_Type()
)
aristaStormControlIfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaStormControlIfDrops.setStatus("current")
_AristaStormControlMibConformance_ObjectIdentity = ObjectIdentity
aristaStormControlMibConformance = _AristaStormControlMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 35, 2)
)
_AristaStormControlMibCompliances_ObjectIdentity = ObjectIdentity
aristaStormControlMibCompliances = _AristaStormControlMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 35, 2, 1)
)
_AristaStormControlMibGroups_ObjectIdentity = ObjectIdentity
aristaStormControlMibGroups = _AristaStormControlMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 35, 2, 2)
)

# Managed Objects groups

aristaStormControlMibInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 35, 2, 2, 1)
)
aristaStormControlMibInterfaceGroup.setObjects(
      *(("ARISTA-STORM-CONTROL-MIB", "aristaStormControlIfThresholdLevel"),
        ("ARISTA-STORM-CONTROL-MIB", "aristaStormControlIfThresholdUnits"),
        ("ARISTA-STORM-CONTROL-MIB", "aristaStormControlIfDrops"))
)
if mibBuilder.loadTexts:
    aristaStormControlMibInterfaceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaStormControlMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 35, 2, 1, 1)
)
aristaStormControlMibCompliance.setObjects(
    ("ARISTA-STORM-CONTROL-MIB", "aristaStormControlMibInterfaceGroup")
)
if mibBuilder.loadTexts:
    aristaStormControlMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-STORM-CONTROL-MIB",
    **{"AristaStormControlTrafficClass": AristaStormControlTrafficClass,
       "AristaStormControlThresholdUnits": AristaStormControlThresholdUnits,
       "aristaStormControlMIB": aristaStormControlMIB,
       "aristaStormControlMibNotifications": aristaStormControlMibNotifications,
       "aristaStormControlMibObjects": aristaStormControlMibObjects,
       "aristaStormControlIfTable": aristaStormControlIfTable,
       "aristaStormControlIfEntry": aristaStormControlIfEntry,
       "aristaStormControlIfTrafficClass": aristaStormControlIfTrafficClass,
       "aristaStormControlIfThresholdLevel": aristaStormControlIfThresholdLevel,
       "aristaStormControlIfThresholdUnits": aristaStormControlIfThresholdUnits,
       "aristaStormControlIfDrops": aristaStormControlIfDrops,
       "aristaStormControlMibConformance": aristaStormControlMibConformance,
       "aristaStormControlMibCompliances": aristaStormControlMibCompliances,
       "aristaStormControlMibCompliance": aristaStormControlMibCompliance,
       "aristaStormControlMibGroups": aristaStormControlMibGroups,
       "aristaStormControlMibInterfaceGroup": aristaStormControlMibInterfaceGroup}
)
