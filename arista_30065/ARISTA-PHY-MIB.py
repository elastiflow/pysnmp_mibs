# SNMP MIB module (ARISTA-PHY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-PHY-MIB.mib
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

aristaPhyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 37)
)
if mibBuilder.loadTexts:
    aristaPhyMIB.setRevisions(
        ("2025-01-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class L1TelemetryDataScale(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("yocto", 1),
          ("zepto", 2),
          ("atto", 3),
          ("femto", 4),
          ("pico", 5),
          ("nano", 6),
          ("micro", 7),
          ("milli", 8),
          ("units", 9))
    )



class L1TelemetryPrecision(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9, 9),
    )



class L1TelemetryValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_AristaPhyIntfTable_Object = MibTable
aristaPhyIntfTable = _AristaPhyIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 37, 1)
)
if mibBuilder.loadTexts:
    aristaPhyIntfTable.setStatus("current")
_AristaPhyIntfEntry_Object = MibTableRow
aristaPhyIntfEntry = _AristaPhyIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 37, 1, 1)
)
aristaPhyIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aristaPhyIntfEntry.setStatus("current")


class _AristaPhyIntfCapabilitiesMap_Type(Bits):
    """Custom type aristaPhyIntfCapabilitiesMap based on Bits"""
    namedValues = NamedValues(
        *(("pcsBer", 0),
          ("preFecBer", 1),
          ("fecUncorrectedCodewords", 2),
          ("phyStateChangeCount", 3))
    )

_AristaPhyIntfCapabilitiesMap_Type.__name__ = "Bits"
_AristaPhyIntfCapabilitiesMap_Object = MibTableColumn
aristaPhyIntfCapabilitiesMap = _AristaPhyIntfCapabilitiesMap_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 37, 1, 1, 1),
    _AristaPhyIntfCapabilitiesMap_Type()
)
aristaPhyIntfCapabilitiesMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaPhyIntfCapabilitiesMap.setStatus("current")
_AristaPhyIntfPcsBer_Type = Counter64
_AristaPhyIntfPcsBer_Object = MibTableColumn
aristaPhyIntfPcsBer = _AristaPhyIntfPcsBer_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 37, 1, 1, 2),
    _AristaPhyIntfPcsBer_Type()
)
aristaPhyIntfPcsBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaPhyIntfPcsBer.setStatus("current")
_AristaPhyIntfPreFecBer_Type = L1TelemetryValue
_AristaPhyIntfPreFecBer_Object = MibTableColumn
aristaPhyIntfPreFecBer = _AristaPhyIntfPreFecBer_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 37, 1, 1, 3),
    _AristaPhyIntfPreFecBer_Type()
)
aristaPhyIntfPreFecBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaPhyIntfPreFecBer.setStatus("current")
_AristaPhyIntfPreFecBerPrecision_Type = L1TelemetryPrecision
_AristaPhyIntfPreFecBerPrecision_Object = MibTableColumn
aristaPhyIntfPreFecBerPrecision = _AristaPhyIntfPreFecBerPrecision_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 37, 1, 1, 4),
    _AristaPhyIntfPreFecBerPrecision_Type()
)
aristaPhyIntfPreFecBerPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaPhyIntfPreFecBerPrecision.setStatus("current")
_AristaPhyIntfPreFecBerDataScale_Type = L1TelemetryDataScale
_AristaPhyIntfPreFecBerDataScale_Object = MibTableColumn
aristaPhyIntfPreFecBerDataScale = _AristaPhyIntfPreFecBerDataScale_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 37, 1, 1, 5),
    _AristaPhyIntfPreFecBerDataScale_Type()
)
aristaPhyIntfPreFecBerDataScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaPhyIntfPreFecBerDataScale.setStatus("current")
_AristaPhyIntfFecUncorrectedCodewords_Type = Counter64
_AristaPhyIntfFecUncorrectedCodewords_Object = MibTableColumn
aristaPhyIntfFecUncorrectedCodewords = _AristaPhyIntfFecUncorrectedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 37, 1, 1, 6),
    _AristaPhyIntfFecUncorrectedCodewords_Type()
)
aristaPhyIntfFecUncorrectedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaPhyIntfFecUncorrectedCodewords.setStatus("current")
_AristaPhyIntfStateChangeCount_Type = Counter64
_AristaPhyIntfStateChangeCount_Object = MibTableColumn
aristaPhyIntfStateChangeCount = _AristaPhyIntfStateChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 37, 1, 1, 7),
    _AristaPhyIntfStateChangeCount_Type()
)
aristaPhyIntfStateChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaPhyIntfStateChangeCount.setStatus("current")
_AristaPhyMibConformance_ObjectIdentity = ObjectIdentity
aristaPhyMibConformance = _AristaPhyMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 37, 3)
)
_AristaPhyMibCompliances_ObjectIdentity = ObjectIdentity
aristaPhyMibCompliances = _AristaPhyMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 37, 3, 1)
)
_AristaPhyMibGroups_ObjectIdentity = ObjectIdentity
aristaPhyMibGroups = _AristaPhyMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 37, 3, 2)
)

# Managed Objects groups

aristaPhyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 37, 3, 2, 1)
)
aristaPhyGroup.setObjects(
      *(("ARISTA-PHY-MIB", "aristaPhyIntfCapabilitiesMap"),
        ("ARISTA-PHY-MIB", "aristaPhyIntfPcsBer"),
        ("ARISTA-PHY-MIB", "aristaPhyIntfPreFecBer"),
        ("ARISTA-PHY-MIB", "aristaPhyIntfPreFecBerPrecision"),
        ("ARISTA-PHY-MIB", "aristaPhyIntfPreFecBerDataScale"),
        ("ARISTA-PHY-MIB", "aristaPhyIntfFecUncorrectedCodewords"),
        ("ARISTA-PHY-MIB", "aristaPhyIntfStateChangeCount"))
)
if mibBuilder.loadTexts:
    aristaPhyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaPhyMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 37, 3, 1, 1)
)
aristaPhyMibCompliance.setObjects(
    ("ARISTA-PHY-MIB", "aristaPhyGroup")
)
if mibBuilder.loadTexts:
    aristaPhyMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-PHY-MIB",
    **{"L1TelemetryDataScale": L1TelemetryDataScale,
       "L1TelemetryPrecision": L1TelemetryPrecision,
       "L1TelemetryValue": L1TelemetryValue,
       "aristaPhyMIB": aristaPhyMIB,
       "aristaPhyIntfTable": aristaPhyIntfTable,
       "aristaPhyIntfEntry": aristaPhyIntfEntry,
       "aristaPhyIntfCapabilitiesMap": aristaPhyIntfCapabilitiesMap,
       "aristaPhyIntfPcsBer": aristaPhyIntfPcsBer,
       "aristaPhyIntfPreFecBer": aristaPhyIntfPreFecBer,
       "aristaPhyIntfPreFecBerPrecision": aristaPhyIntfPreFecBerPrecision,
       "aristaPhyIntfPreFecBerDataScale": aristaPhyIntfPreFecBerDataScale,
       "aristaPhyIntfFecUncorrectedCodewords": aristaPhyIntfFecUncorrectedCodewords,
       "aristaPhyIntfStateChangeCount": aristaPhyIntfStateChangeCount,
       "aristaPhyMibConformance": aristaPhyMibConformance,
       "aristaPhyMibCompliances": aristaPhyMibCompliances,
       "aristaPhyMibCompliance": aristaPhyMibCompliance,
       "aristaPhyMibGroups": aristaPhyMibGroups,
       "aristaPhyGroup": aristaPhyGroup}
)
