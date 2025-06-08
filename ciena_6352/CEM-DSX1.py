# SNMP MIB module (CEM-DSX1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-DSX1.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:21 2025
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

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

(dsx1ConfigEntry,) = mibBuilder.importSymbols(
    "DS1-MIB",
    "dsx1ConfigEntry")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
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

cnDsx1Group = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 3)
)
if mibBuilder.loadTexts:
    cnDsx1Group.setRevisions(
        ("2002-02-20 16:36",
         "2001-08-15 12:02",
         "2001-10-22 14:42")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class T1ActiveTimeSource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("t1TimeSourceNotProvisioned", 0),
          ("t1Interface1", 1),
          ("t1Interface2", 2),
          ("t1Interface3", 3),
          ("t1Interface4", 4),
          ("freeRun", 9999))
    )



# MIB Managed Objects in the order of their OIDs

_CnDsx1PrimaryTimingSource_Type = InterfaceIndexOrZero
_CnDsx1PrimaryTimingSource_Object = MibScalar
cnDsx1PrimaryTimingSource = _CnDsx1PrimaryTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 6352, 3, 1),
    _CnDsx1PrimaryTimingSource_Type()
)
cnDsx1PrimaryTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDsx1PrimaryTimingSource.setStatus("obsolete")
_CnDsx1SecondaryTimingSource_Type = InterfaceIndexOrZero
_CnDsx1SecondaryTimingSource_Object = MibScalar
cnDsx1SecondaryTimingSource = _CnDsx1SecondaryTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 6352, 3, 2),
    _CnDsx1SecondaryTimingSource_Type()
)
cnDsx1SecondaryTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDsx1SecondaryTimingSource.setStatus("obsolete")
_CnDsx1ActiveTimingSource_Type = T1ActiveTimeSource
_CnDsx1ActiveTimingSource_Object = MibScalar
cnDsx1ActiveTimingSource = _CnDsx1ActiveTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 6352, 3, 3),
    _CnDsx1ActiveTimingSource_Type()
)
cnDsx1ActiveTimingSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnDsx1ActiveTimingSource.setStatus("current")
_CnDsx1ifXTable_Object = MibTable
cnDsx1ifXTable = _CnDsx1ifXTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 3, 4)
)
if mibBuilder.loadTexts:
    cnDsx1ifXTable.setStatus("current")
_CnDsx1ifXEntry_Object = MibTableRow
cnDsx1ifXEntry = _CnDsx1ifXEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 3, 4, 1)
)
cnDsx1ifXEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cnDsx1ifXEntry.setStatus("current")


class _CnDsx1LineBuildOut_Type(Integer32):
    """Custom type cnDsx1LineBuildOut based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("longHaul0dB", 1),
          ("longHaul7-5dB", 2),
          ("longHaul15dB", 3),
          ("longHaul22-5dB", 4),
          ("shortHaul0-110ft", 5),
          ("shortHaul110-220ft", 6),
          ("shortHaul220-330ft", 7),
          ("shortHaul330-440ft", 8),
          ("shortHaul440-550ft", 9),
          ("shortHaul550-660ft", 10),
          ("etsi120ohm", 11),
          ("etsi75ohm", 12),
          ("unsupportedLbo", 13))
    )


_CnDsx1LineBuildOut_Type.__name__ = "Integer32"
_CnDsx1LineBuildOut_Object = MibTableColumn
cnDsx1LineBuildOut = _CnDsx1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 6352, 3, 4, 1, 1),
    _CnDsx1LineBuildOut_Type()
)
cnDsx1LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDsx1LineBuildOut.setStatus("current")
_CnDsx1Conformance_ObjectIdentity = ObjectIdentity
cnDsx1Conformance = _CnDsx1Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 3, 6)
)
_CnDsx1LineConfigTable_Object = MibTable
cnDsx1LineConfigTable = _CnDsx1LineConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 3, 7)
)
if mibBuilder.loadTexts:
    cnDsx1LineConfigTable.setStatus("current")
_CnDsx1LineConfigEntry_Object = MibTableRow
cnDsx1LineConfigEntry = _CnDsx1LineConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 3, 7, 1)
)
if mibBuilder.loadTexts:
    cnDsx1LineConfigEntry.setStatus("current")


class _CnDsx1LineType_Type(Integer32):
    """Custom type cnDsx1LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2048)
        )
    )
    namedValues = NamedValues(
        *(("cnDsx1Other", 1),
          ("cnDsx1Slc96", 2048))
    )


_CnDsx1LineType_Type.__name__ = "Integer32"
_CnDsx1LineType_Object = MibTableColumn
cnDsx1LineType = _CnDsx1LineType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 3, 7, 1, 1),
    _CnDsx1LineType_Type()
)
cnDsx1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnDsx1LineType.setStatus("current")
dsx1ConfigEntry.registerAugmentions(
    ("CEM-DSX1",
     "cnDsx1LineConfigEntry")
)
cnDsx1LineConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())

# Managed Objects groups

cnDsx1ObjectsForCNX510AndCNX511 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 3, 6, 2)
)
cnDsx1ObjectsForCNX510AndCNX511.setObjects(
      *(("CEM-DSX1", "cnDsx1PrimaryTimingSource"),
        ("CEM-DSX1", "cnDsx1SecondaryTimingSource"),
        ("CEM-DSX1", "cnDsx1ActiveTimingSource"),
        ("CEM-DSX1", "cnDsx1LineBuildOut"),
        ("CEM-DSX1", "cnDsx1LineType"))
)
if mibBuilder.loadTexts:
    cnDsx1ObjectsForCNX510AndCNX511.setStatus("obsolete")

cnDsx1ObjectsForCN1000 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 3, 6, 3)
)
cnDsx1ObjectsForCN1000.setObjects(
      *(("CEM-DSX1", "cnDsx1LineBuildOut"),
        ("CEM-DSX1", "cnDsx1LineType"))
)
if mibBuilder.loadTexts:
    cnDsx1ObjectsForCN1000.setStatus("current")


# Notification objects

timingSourceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 3, 5)
)
timingSourceChange.setObjects(
    ("CEM-DSX1", "cnDsx1ActiveTimingSource")
)
if mibBuilder.loadTexts:
    timingSourceChange.setStatus(
        "current"
    )


# Notifications groups

cnDsx1NotificationsForCNX510AndCNX511 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6352, 3, 6, 1)
)
cnDsx1NotificationsForCNX510AndCNX511.setObjects(
    ("CEM-DSX1", "timingSourceChange")
)
if mibBuilder.loadTexts:
    cnDsx1NotificationsForCNX510AndCNX511.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-DSX1",
    **{"T1ActiveTimeSource": T1ActiveTimeSource,
       "cnDsx1Group": cnDsx1Group,
       "cnDsx1PrimaryTimingSource": cnDsx1PrimaryTimingSource,
       "cnDsx1SecondaryTimingSource": cnDsx1SecondaryTimingSource,
       "cnDsx1ActiveTimingSource": cnDsx1ActiveTimingSource,
       "cnDsx1ifXTable": cnDsx1ifXTable,
       "cnDsx1ifXEntry": cnDsx1ifXEntry,
       "cnDsx1LineBuildOut": cnDsx1LineBuildOut,
       "timingSourceChange": timingSourceChange,
       "cnDsx1Conformance": cnDsx1Conformance,
       "cnDsx1NotificationsForCNX510AndCNX511": cnDsx1NotificationsForCNX510AndCNX511,
       "cnDsx1ObjectsForCNX510AndCNX511": cnDsx1ObjectsForCNX510AndCNX511,
       "cnDsx1ObjectsForCN1000": cnDsx1ObjectsForCN1000,
       "cnDsx1LineConfigTable": cnDsx1LineConfigTable,
       "cnDsx1LineConfigEntry": cnDsx1LineConfigEntry,
       "cnDsx1LineType": cnDsx1LineType}
)
