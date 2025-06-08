# SNMP MIB module (A3COM-HUAWEI-E1T1VI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-E1T1VI-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:04:11 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

h3cE1T1VI = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 76)
)
if mibBuilder.loadTexts:
    h3cE1T1VI.setRevisions(
        ("2010-04-08 18:55",
         "2009-06-08 17:41",
         "2007-04-05 15:42")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cE1T1VITable_Object = MibTable
h3cE1T1VITable = _H3cE1T1VITable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 76, 1)
)
if mibBuilder.loadTexts:
    h3cE1T1VITable.setStatus("current")
_H3cE1T1VIEntry_Object = MibTableRow
h3cE1T1VIEntry = _H3cE1T1VIEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 76, 1, 1)
)
h3cE1T1VIEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cE1T1VIEntry.setStatus("current")
_H3cE1T1VIUsingTimeslots_Type = Integer32
_H3cE1T1VIUsingTimeslots_Object = MibTableColumn
h3cE1T1VIUsingTimeslots = _H3cE1T1VIUsingTimeslots_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 76, 1, 1, 1),
    _H3cE1T1VIUsingTimeslots_Type()
)
h3cE1T1VIUsingTimeslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cE1T1VIUsingTimeslots.setStatus("current")
_H3cE1T1VIUsingTimeslotsRatio_Type = Integer32
_H3cE1T1VIUsingTimeslotsRatio_Object = MibTableColumn
h3cE1T1VIUsingTimeslotsRatio = _H3cE1T1VIUsingTimeslotsRatio_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 76, 1, 1, 2),
    _H3cE1T1VIUsingTimeslotsRatio_Type()
)
h3cE1T1VIUsingTimeslotsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cE1T1VIUsingTimeslotsRatio.setStatus("current")
_H3cE1T1VINotifications_ObjectIdentity = ObjectIdentity
h3cE1T1VINotifications = _H3cE1T1VINotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 76, 2)
)
_H3cE1T1VITrapPrefix_ObjectIdentity = ObjectIdentity
h3cE1T1VITrapPrefix = _H3cE1T1VITrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 76, 2, 0)
)
_H3cE1T1VIGeneral_ObjectIdentity = ObjectIdentity
h3cE1T1VIGeneral = _H3cE1T1VIGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 76, 3)
)


class _H3cE1T1VITrapTimeSlotEnable_Type(Integer32):
    """Custom type h3cE1T1VITrapTimeSlotEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_H3cE1T1VITrapTimeSlotEnable_Type.__name__ = "Integer32"
_H3cE1T1VITrapTimeSlotEnable_Object = MibScalar
h3cE1T1VITrapTimeSlotEnable = _H3cE1T1VITrapTimeSlotEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 76, 3, 1),
    _H3cE1T1VITrapTimeSlotEnable_Type()
)
h3cE1T1VITrapTimeSlotEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cE1T1VITrapTimeSlotEnable.setStatus("current")

# Managed Objects groups


# Notification objects

h3cE1T1VITrapTimeSlot = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 76, 2, 0, 1)
)
h3cE1T1VITrapTimeSlot.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cE1T1VITrapTimeSlot.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-E1T1VI-MIB",
    **{"h3cE1T1VI": h3cE1T1VI,
       "h3cE1T1VITable": h3cE1T1VITable,
       "h3cE1T1VIEntry": h3cE1T1VIEntry,
       "h3cE1T1VIUsingTimeslots": h3cE1T1VIUsingTimeslots,
       "h3cE1T1VIUsingTimeslotsRatio": h3cE1T1VIUsingTimeslotsRatio,
       "h3cE1T1VINotifications": h3cE1T1VINotifications,
       "h3cE1T1VITrapPrefix": h3cE1T1VITrapPrefix,
       "h3cE1T1VITrapTimeSlot": h3cE1T1VITrapTimeSlot,
       "h3cE1T1VIGeneral": h3cE1T1VIGeneral,
       "h3cE1T1VITrapTimeSlotEnable": h3cE1T1VITrapTimeSlotEnable}
)
