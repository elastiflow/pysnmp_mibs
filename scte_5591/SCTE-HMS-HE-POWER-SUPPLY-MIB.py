# SNMP MIB module (SCTE-HMS-HE-POWER-SUPPLY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-HE-POWER-SUPPLY-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:31:48 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(HeHundredthWatts,
 HeMilliAmp,
 HeTenthVolt,
 hePowerSupply) = mibBuilder.importSymbols(
    "SCTE-HMS-HEADENDIDENT-MIB",
    "HeHundredthWatts",
    "HeMilliAmp",
    "HeTenthVolt",
    "hePowerSupply")

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

hePowerSupplyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HePsMIBObjects_ObjectIdentity = ObjectIdentity
hePsMIBObjects = _HePsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 1)
)
_HePsUnitTable_Object = MibTable
hePsUnitTable = _HePsUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hePsUnitTable.setStatus("current")
_HePsUnitEntry_Object = MibTableRow
hePsUnitEntry = _HePsUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 1, 1, 1)
)
hePsUnitEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hePsUnitEntry.setStatus("current")
_HePsUnitCurrentIN_Type = HeMilliAmp
_HePsUnitCurrentIN_Object = MibTableColumn
hePsUnitCurrentIN = _HePsUnitCurrentIN_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 1, 1, 1, 1),
    _HePsUnitCurrentIN_Type()
)
hePsUnitCurrentIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hePsUnitCurrentIN.setStatus("current")
if mibBuilder.loadTexts:
    hePsUnitCurrentIN.setUnits("milliamperes")
_HePsUnitPowerIN_Type = HeHundredthWatts
_HePsUnitPowerIN_Object = MibTableColumn
hePsUnitPowerIN = _HePsUnitPowerIN_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 1, 1, 1, 2),
    _HePsUnitPowerIN_Type()
)
hePsUnitPowerIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hePsUnitPowerIN.setStatus("current")
if mibBuilder.loadTexts:
    hePsUnitPowerIN.setUnits("hundredths of a watt")
_HePsUnitDescription_Type = DisplayString
_HePsUnitDescription_Object = MibTableColumn
hePsUnitDescription = _HePsUnitDescription_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 1, 1, 1, 3),
    _HePsUnitDescription_Type()
)
hePsUnitDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hePsUnitDescription.setStatus("current")
_HePsUnitVoltageIN_Type = HeTenthVolt
_HePsUnitVoltageIN_Object = MibTableColumn
hePsUnitVoltageIN = _HePsUnitVoltageIN_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 1, 1, 1, 4),
    _HePsUnitVoltageIN_Type()
)
hePsUnitVoltageIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hePsUnitVoltageIN.setStatus("current")
if mibBuilder.loadTexts:
    hePsUnitVoltageIN.setUnits("tenths of a volt")
_HePsOutputTable_Object = MibTable
hePsOutputTable = _HePsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hePsOutputTable.setStatus("current")
_HePsOutputEntry_Object = MibTableRow
hePsOutputEntry = _HePsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 1, 2, 1)
)
hePsOutputEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-HE-POWER-SUPPLY-MIB", "hePsOutputIndex"),
)
if mibBuilder.loadTexts:
    hePsOutputEntry.setStatus("current")
_HePsOutputIndex_Type = Unsigned32
_HePsOutputIndex_Object = MibTableColumn
hePsOutputIndex = _HePsOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 1, 2, 1, 1),
    _HePsOutputIndex_Type()
)
hePsOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hePsOutputIndex.setStatus("current")
_HePsOutputVoltage_Type = HeTenthVolt
_HePsOutputVoltage_Object = MibTableColumn
hePsOutputVoltage = _HePsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 1, 2, 1, 2),
    _HePsOutputVoltage_Type()
)
hePsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hePsOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    hePsOutputVoltage.setUnits("tenths of a volt")
_HePsOutputCurrent_Type = HeMilliAmp
_HePsOutputCurrent_Object = MibTableColumn
hePsOutputCurrent = _HePsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 1, 2, 1, 3),
    _HePsOutputCurrent_Type()
)
hePsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hePsOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    hePsOutputCurrent.setUnits("milliamperes")
_HePsOutputPower_Type = HeHundredthWatts
_HePsOutputPower_Object = MibTableColumn
hePsOutputPower = _HePsOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 1, 2, 1, 4),
    _HePsOutputPower_Type()
)
hePsOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hePsOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    hePsOutputPower.setUnits("hundredths of a watt")
_HePsMIBConformance_ObjectIdentity = ObjectIdentity
hePsMIBConformance = _HePsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 2)
)
_HePsMIBCompliances_ObjectIdentity = ObjectIdentity
hePsMIBCompliances = _HePsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 2, 1)
)
_HePsMIBGroups_ObjectIdentity = ObjectIdentity
hePsMIBGroups = _HePsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 2, 2)
)

# Managed Objects groups

hePsOutputMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 2, 2, 1)
)
hePsOutputMandatoryGroup.setObjects(
    ("SCTE-HMS-HE-POWER-SUPPLY-MIB", "hePsOutputVoltage")
)
if mibBuilder.loadTexts:
    hePsOutputMandatoryGroup.setStatus("current")

hePsUnitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 2, 2, 2)
)
hePsUnitGroup.setObjects(
      *(("SCTE-HMS-HE-POWER-SUPPLY-MIB", "hePsUnitVoltageIN"),
        ("SCTE-HMS-HE-POWER-SUPPLY-MIB", "hePsUnitCurrentIN"),
        ("SCTE-HMS-HE-POWER-SUPPLY-MIB", "hePsUnitPowerIN"),
        ("SCTE-HMS-HE-POWER-SUPPLY-MIB", "hePsUnitDescription"))
)
if mibBuilder.loadTexts:
    hePsUnitGroup.setStatus("current")

hePsOutputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 2, 2, 3)
)
hePsOutputGroup.setObjects(
      *(("SCTE-HMS-HE-POWER-SUPPLY-MIB", "hePsOutputCurrent"),
        ("SCTE-HMS-HE-POWER-SUPPLY-MIB", "hePsOutputPower"))
)
if mibBuilder.loadTexts:
    hePsOutputGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hePsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2, 1, 2, 1, 1)
)
hePsCompliance.setObjects(
      *(("SCTE-HMS-HE-POWER-SUPPLY-MIB", "hePsOutputMandatoryGroup"),
        ("SCTE-HMS-HE-POWER-SUPPLY-MIB", "hePsUnitGroup"),
        ("SCTE-HMS-HE-POWER-SUPPLY-MIB", "hePsOutputGroup"))
)
if mibBuilder.loadTexts:
    hePsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-HE-POWER-SUPPLY-MIB",
    **{"hePowerSupplyMIB": hePowerSupplyMIB,
       "hePsMIBObjects": hePsMIBObjects,
       "hePsUnitTable": hePsUnitTable,
       "hePsUnitEntry": hePsUnitEntry,
       "hePsUnitCurrentIN": hePsUnitCurrentIN,
       "hePsUnitPowerIN": hePsUnitPowerIN,
       "hePsUnitDescription": hePsUnitDescription,
       "hePsUnitVoltageIN": hePsUnitVoltageIN,
       "hePsOutputTable": hePsOutputTable,
       "hePsOutputEntry": hePsOutputEntry,
       "hePsOutputIndex": hePsOutputIndex,
       "hePsOutputVoltage": hePsOutputVoltage,
       "hePsOutputCurrent": hePsOutputCurrent,
       "hePsOutputPower": hePsOutputPower,
       "hePsMIBConformance": hePsMIBConformance,
       "hePsMIBCompliances": hePsMIBCompliances,
       "hePsCompliance": hePsCompliance,
       "hePsMIBGroups": hePsMIBGroups,
       "hePsOutputMandatoryGroup": hePsOutputMandatoryGroup,
       "hePsUnitGroup": hePsUnitGroup,
       "hePsOutputGroup": hePsOutputGroup}
)
