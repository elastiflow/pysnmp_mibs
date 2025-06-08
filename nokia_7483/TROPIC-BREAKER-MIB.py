# SNMP MIB module (TROPIC-BREAKER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-BREAKER-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:06:37 2025
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

(tnBreakerMIB,
 tnMiscModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnBreakerMIB",
    "tnMiscModules")

(tnShelfIndex,) = mibBuilder.importSymbols(
    "TROPIC-SHELF-MIB",
    "tnShelfIndex")

(tnSlotIndex,) = mibBuilder.importSymbols(
    "TROPIC-SLOT-MIB",
    "tnSlotIndex")


# MODULE-IDENTITY

tnBreakerMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    tnBreakerMibModule.setRevisions(
        ("2009-08-13 12:00",
         "2010-10-18 12:00",
         "2011-04-14 12:00",
         "2011-05-23 12:00",
         "2012-09-13 12:00",
         "2013-05-21 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnBreakerConf_ObjectIdentity = ObjectIdentity
tnBreakerConf = _TnBreakerConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 1)
)
_TnBreakerGroups_ObjectIdentity = ObjectIdentity
tnBreakerGroups = _TnBreakerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 1, 1)
)
_TnBreakerCompliances_ObjectIdentity = ObjectIdentity
tnBreakerCompliances = _TnBreakerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 1, 2)
)
_TnBreakerObjs_ObjectIdentity = ObjectIdentity
tnBreakerObjs = _TnBreakerObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 2)
)
_TnBreakerBasics_ObjectIdentity = ObjectIdentity
tnBreakerBasics = _TnBreakerBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 2, 1)
)
_TnPowerFilterTable_Object = MibTable
tnPowerFilterTable = _TnPowerFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnPowerFilterTable.setStatus("current")
_TnPowerFilterEntry_Object = MibTableRow
tnPowerFilterEntry = _TnPowerFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 2, 1, 2, 1)
)
tnPowerFilterEntry.setIndexNames(
    (0, "TROPIC-SHELF-MIB", "tnShelfIndex"),
    (0, "TROPIC-SLOT-MIB", "tnSlotIndex"),
)
if mibBuilder.loadTexts:
    tnPowerFilterEntry.setStatus("current")


class _TnPowerFilterAmpRating_Type(Integer32):
    """Custom type tnPowerFilterAmpRating based on Integer32"""
    defaultValue = 0


_TnPowerFilterAmpRating_Type.__name__ = "Integer32"
_TnPowerFilterAmpRating_Object = MibTableColumn
tnPowerFilterAmpRating = _TnPowerFilterAmpRating_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 2, 1, 2, 1, 1),
    _TnPowerFilterAmpRating_Type()
)
tnPowerFilterAmpRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerFilterAmpRating.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerFilterAmpRating.setUnits("1/10 amps")


class _TnPowerFilterCardPower_Type(OctetString):
    """Custom type tnPowerFilterCardPower based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_TnPowerFilterCardPower_Type.__name__ = "OctetString"
_TnPowerFilterCardPower_Object = MibTableColumn
tnPowerFilterCardPower = _TnPowerFilterCardPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 2, 1, 2, 1, 2),
    _TnPowerFilterCardPower_Type()
)
tnPowerFilterCardPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPowerFilterCardPower.setStatus("current")
if mibBuilder.loadTexts:
    tnPowerFilterCardPower.setUnits("watts")

# Managed Objects groups

tnPowerFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 1, 1, 2)
)
tnPowerFilterGroup.setObjects(
      *(("TROPIC-BREAKER-MIB", "tnPowerFilterAmpRating"),
        ("TROPIC-BREAKER-MIB", "tnPowerFilterCardPower"))
)
if mibBuilder.loadTexts:
    tnPowerFilterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnBreakerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 1, 2, 1)
)
tnBreakerCompliance.setObjects(
    ("TROPIC-BREAKER-MIB", "tnPowerFilterGroup")
)
if mibBuilder.loadTexts:
    tnBreakerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-BREAKER-MIB",
    **{"tnBreakerMibModule": tnBreakerMibModule,
       "tnBreakerConf": tnBreakerConf,
       "tnBreakerGroups": tnBreakerGroups,
       "tnPowerFilterGroup": tnPowerFilterGroup,
       "tnBreakerCompliances": tnBreakerCompliances,
       "tnBreakerCompliance": tnBreakerCompliance,
       "tnBreakerObjs": tnBreakerObjs,
       "tnBreakerBasics": tnBreakerBasics,
       "tnPowerFilterTable": tnPowerFilterTable,
       "tnPowerFilterEntry": tnPowerFilterEntry,
       "tnPowerFilterAmpRating": tnPowerFilterAmpRating,
       "tnPowerFilterCardPower": tnPowerFilterCardPower}
)
