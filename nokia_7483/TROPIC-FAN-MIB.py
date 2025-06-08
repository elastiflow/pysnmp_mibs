# SNMP MIB module (TROPIC-FAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-FAN-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:04:18 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(tnFanMIB,
 tnMiscModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnFanMIB",
    "tnMiscModules")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")

(TropicCardCLEI,
 TropicCardHFD,
 TropicCardManufacturingPartNumber,
 TropicCardMarketingPartNumber,
 TropicCardSWGenericLoadName,
 TropicCardSerialNumber,
 TropicLEDColorType,
 TropicLEDStateType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "TropicCardCLEI",
    "TropicCardHFD",
    "TropicCardManufacturingPartNumber",
    "TropicCardMarketingPartNumber",
    "TropicCardSWGenericLoadName",
    "TropicCardSerialNumber",
    "TropicLEDColorType",
    "TropicLEDStateType")


# MODULE-IDENTITY

tnFanMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    tnFanMibModule.setRevisions(
        ("2008-03-20 12:00",
         "2010-02-16 12:00",
         "2013-05-21 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnFanConf_ObjectIdentity = ObjectIdentity
tnFanConf = _TnFanConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 1)
)
_TnFanGroups_ObjectIdentity = ObjectIdentity
tnFanGroups = _TnFanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 1, 1)
)
_TnFanCompliances_ObjectIdentity = ObjectIdentity
tnFanCompliances = _TnFanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 1, 2)
)
_TnFanObjs_ObjectIdentity = ObjectIdentity
tnFanObjs = _TnFanObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 2)
)
_TnFanBasics_ObjectIdentity = ObjectIdentity
tnFanBasics = _TnFanBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 2, 1)
)
_TnFanUnitTable_Object = MibTable
tnFanUnitTable = _TnFanUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnFanUnitTable.setStatus("current")
_TnFanUnitEntry_Object = MibTableRow
tnFanUnitEntry = _TnFanUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 2, 1, 2, 1)
)
tnFanUnitEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnFanUnitEntry.setStatus("current")


class _TnFanUnitName_Type(SnmpAdminString):
    """Custom type tnFanUnitName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TnFanUnitName_Type.__name__ = "SnmpAdminString"
_TnFanUnitName_Object = MibTableColumn
tnFanUnitName = _TnFanUnitName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 2, 1, 2, 1, 1),
    _TnFanUnitName_Type()
)
tnFanUnitName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnFanUnitName.setStatus("current")


class _TnFanUnitDescr_Type(SnmpAdminString):
    """Custom type tnFanUnitDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnFanUnitDescr_Type.__name__ = "SnmpAdminString"
_TnFanUnitDescr_Object = MibTableColumn
tnFanUnitDescr = _TnFanUnitDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 2, 1, 2, 1, 2),
    _TnFanUnitDescr_Type()
)
tnFanUnitDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnFanUnitDescr.setStatus("current")
_TnFanUnitCLEI_Type = TropicCardCLEI
_TnFanUnitCLEI_Object = MibTableColumn
tnFanUnitCLEI = _TnFanUnitCLEI_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 2, 1, 2, 1, 3),
    _TnFanUnitCLEI_Type()
)
tnFanUnitCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFanUnitCLEI.setStatus("current")
_TnFanUnitHFD_Type = TropicCardHFD
_TnFanUnitHFD_Object = MibTableColumn
tnFanUnitHFD = _TnFanUnitHFD_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 2, 1, 2, 1, 4),
    _TnFanUnitHFD_Type()
)
tnFanUnitHFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFanUnitHFD.setStatus("current")
_TnFanUnitSerialNumber_Type = TropicCardSerialNumber
_TnFanUnitSerialNumber_Object = MibTableColumn
tnFanUnitSerialNumber = _TnFanUnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 2, 1, 2, 1, 5),
    _TnFanUnitSerialNumber_Type()
)
tnFanUnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFanUnitSerialNumber.setStatus("current")
_TnFanUnitManufacturingPartNumber_Type = TropicCardManufacturingPartNumber
_TnFanUnitManufacturingPartNumber_Object = MibTableColumn
tnFanUnitManufacturingPartNumber = _TnFanUnitManufacturingPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 2, 1, 2, 1, 6),
    _TnFanUnitManufacturingPartNumber_Type()
)
tnFanUnitManufacturingPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFanUnitManufacturingPartNumber.setStatus("current")
_TnFanUnitMarketingPartNumber_Type = TropicCardMarketingPartNumber
_TnFanUnitMarketingPartNumber_Object = MibTableColumn
tnFanUnitMarketingPartNumber = _TnFanUnitMarketingPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 2, 1, 2, 1, 7),
    _TnFanUnitMarketingPartNumber_Type()
)
tnFanUnitMarketingPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFanUnitMarketingPartNumber.setStatus("current")
_TnFanUnitSWGenericLoadName_Type = TropicCardSWGenericLoadName
_TnFanUnitSWGenericLoadName_Object = MibTableColumn
tnFanUnitSWGenericLoadName = _TnFanUnitSWGenericLoadName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 2, 1, 2, 1, 8),
    _TnFanUnitSWGenericLoadName_Type()
)
tnFanUnitSWGenericLoadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFanUnitSWGenericLoadName.setStatus("current")
_TnFanUnitPower_Type = Integer32
_TnFanUnitPower_Object = MibTableColumn
tnFanUnitPower = _TnFanUnitPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 2, 1, 2, 1, 9),
    _TnFanUnitPower_Type()
)
tnFanUnitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFanUnitPower.setStatus("current")
_TnFanUnitSpeed_Type = Integer32
_TnFanUnitSpeed_Object = MibTableColumn
tnFanUnitSpeed = _TnFanUnitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 2, 1, 2, 1, 10),
    _TnFanUnitSpeed_Type()
)
tnFanUnitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFanUnitSpeed.setStatus("current")
if mibBuilder.loadTexts:
    tnFanUnitSpeed.setUnits("RPM")
_TnFanUnitStatusLEDColor_Type = TropicLEDColorType
_TnFanUnitStatusLEDColor_Object = MibTableColumn
tnFanUnitStatusLEDColor = _TnFanUnitStatusLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 2, 1, 2, 1, 11),
    _TnFanUnitStatusLEDColor_Type()
)
tnFanUnitStatusLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFanUnitStatusLEDColor.setStatus("current")
_TnFanUnitStatusLEDState_Type = TropicLEDStateType
_TnFanUnitStatusLEDState_Object = MibTableColumn
tnFanUnitStatusLEDState = _TnFanUnitStatusLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 2, 1, 2, 1, 12),
    _TnFanUnitStatusLEDState_Type()
)
tnFanUnitStatusLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnFanUnitStatusLEDState.setStatus("current")


class _TnFanUnitSpeedControl_Type(Integer32):
    """Custom type tnFanUnitSpeedControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("maximum", 2))
    )


_TnFanUnitSpeedControl_Type.__name__ = "Integer32"
_TnFanUnitSpeedControl_Object = MibTableColumn
tnFanUnitSpeedControl = _TnFanUnitSpeedControl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 2, 1, 2, 1, 13),
    _TnFanUnitSpeedControl_Type()
)
tnFanUnitSpeedControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnFanUnitSpeedControl.setStatus("current")

# Managed Objects groups

tnFanUnitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 1, 1, 2)
)
tnFanUnitGroup.setObjects(
      *(("TROPIC-FAN-MIB", "tnFanUnitName"),
        ("TROPIC-FAN-MIB", "tnFanUnitDescr"),
        ("TROPIC-FAN-MIB", "tnFanUnitCLEI"),
        ("TROPIC-FAN-MIB", "tnFanUnitHFD"),
        ("TROPIC-FAN-MIB", "tnFanUnitSerialNumber"),
        ("TROPIC-FAN-MIB", "tnFanUnitManufacturingPartNumber"),
        ("TROPIC-FAN-MIB", "tnFanUnitMarketingPartNumber"),
        ("TROPIC-FAN-MIB", "tnFanUnitSWGenericLoadName"),
        ("TROPIC-FAN-MIB", "tnFanUnitPower"),
        ("TROPIC-FAN-MIB", "tnFanUnitSpeed"),
        ("TROPIC-FAN-MIB", "tnFanUnitStatusLEDColor"),
        ("TROPIC-FAN-MIB", "tnFanUnitStatusLEDState"),
        ("TROPIC-FAN-MIB", "tnFanUnitSpeedControl"))
)
if mibBuilder.loadTexts:
    tnFanUnitGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnFanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 1, 1, 2, 1)
)
tnFanCompliance.setObjects(
    ("TROPIC-FAN-MIB", "tnFanUnitGroup")
)
if mibBuilder.loadTexts:
    tnFanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-FAN-MIB",
    **{"tnFanMibModule": tnFanMibModule,
       "tnFanConf": tnFanConf,
       "tnFanGroups": tnFanGroups,
       "tnFanUnitGroup": tnFanUnitGroup,
       "tnFanCompliances": tnFanCompliances,
       "tnFanCompliance": tnFanCompliance,
       "tnFanObjs": tnFanObjs,
       "tnFanBasics": tnFanBasics,
       "tnFanUnitTable": tnFanUnitTable,
       "tnFanUnitEntry": tnFanUnitEntry,
       "tnFanUnitName": tnFanUnitName,
       "tnFanUnitDescr": tnFanUnitDescr,
       "tnFanUnitCLEI": tnFanUnitCLEI,
       "tnFanUnitHFD": tnFanUnitHFD,
       "tnFanUnitSerialNumber": tnFanUnitSerialNumber,
       "tnFanUnitManufacturingPartNumber": tnFanUnitManufacturingPartNumber,
       "tnFanUnitMarketingPartNumber": tnFanUnitMarketingPartNumber,
       "tnFanUnitSWGenericLoadName": tnFanUnitSWGenericLoadName,
       "tnFanUnitPower": tnFanUnitPower,
       "tnFanUnitSpeed": tnFanUnitSpeed,
       "tnFanUnitStatusLEDColor": tnFanUnitStatusLEDColor,
       "tnFanUnitStatusLEDState": tnFanUnitStatusLEDState,
       "tnFanUnitSpeedControl": tnFanUnitSpeedControl}
)
