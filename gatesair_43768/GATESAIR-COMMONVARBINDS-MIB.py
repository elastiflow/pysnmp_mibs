# SNMP MIB module (GATESAIR-COMMONVARBINDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gatesair_43768/GATESAIR-COMMONVARBINDS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:03:36 2025
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

(gatesAirGeneric,
 gatesAirMibs,
 gatesAirSmi,
 intraplexGeneric,
 intraplexMibs,
 modulations,
 transmissionMibs) = mibBuilder.importSymbols(
    "GATESAIR-SMI",
    "gatesAirGeneric",
    "gatesAirMibs",
    "gatesAirSmi",
    "intraplexGeneric",
    "intraplexMibs",
    "modulations",
    "transmissionMibs")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

gatesAirCommonVarbinds = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 1, 4)
)
if mibBuilder.loadTexts:
    gatesAirCommonVarbinds.setRevisions(
        ("2014-12-16 15:33",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CommonVarbinds_ObjectIdentity = ObjectIdentity
commonVarbinds = _CommonVarbinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 3)
)
if mibBuilder.loadTexts:
    commonVarbinds.setStatus("current")
_EventVarbinds_ObjectIdentity = ObjectIdentity
eventVarbinds = _EventVarbinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 3, 1)
)
_EventCount_Type = Counter32
_EventCount_Object = MibScalar
eventCount = _EventCount_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 3, 1, 1),
    _EventCount_Type()
)
eventCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventCount.setStatus("current")


class _EventPriority_Type(Integer32):
    """Custom type eventPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 1),
          ("warning", 2))
    )


_EventPriority_Type.__name__ = "Integer32"
_EventPriority_Object = MibScalar
eventPriority = _EventPriority_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 3, 1, 2),
    _EventPriority_Type()
)
eventPriority.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventPriority.setStatus("current")
_EventTimeStamp_Type = DateAndTime
_EventTimeStamp_Object = MibScalar
eventTimeStamp = _EventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 3, 1, 3),
    _EventTimeStamp_Type()
)
eventTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTimeStamp.setStatus("current")
_EventDescription_Type = OctetString
_EventDescription_Object = MibScalar
eventDescription = _EventDescription_Object(
    (1, 3, 6, 1, 4, 1, 43768, 2, 3, 1, 4),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventDescription.setStatus("current")
_CommonVarbindsConf_ObjectIdentity = ObjectIdentity
commonVarbindsConf = _CommonVarbindsConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43768, 2, 3, 2)
)

# Managed Objects groups

commonVarbindsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43768, 2, 3, 2, 1)
)
commonVarbindsObjectGroup.setObjects(
      *(("GATESAIR-COMMONVARBINDS-MIB", "eventCount"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventPriority"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("GATESAIR-COMMONVARBINDS-MIB", "eventDescription"))
)
if mibBuilder.loadTexts:
    commonVarbindsObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

commonVarbindCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43768, 2, 3, 2, 2)
)
commonVarbindCompliance.setObjects(
    ("GATESAIR-COMMONVARBINDS-MIB", "commonVarbindsObjectGroup")
)
if mibBuilder.loadTexts:
    commonVarbindCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GATESAIR-COMMONVARBINDS-MIB",
    **{"gatesAirCommonVarbinds": gatesAirCommonVarbinds,
       "commonVarbinds": commonVarbinds,
       "eventVarbinds": eventVarbinds,
       "eventCount": eventCount,
       "eventPriority": eventPriority,
       "eventTimeStamp": eventTimeStamp,
       "eventDescription": eventDescription,
       "commonVarbindsConf": commonVarbindsConf,
       "commonVarbindsObjectGroup": commonVarbindsObjectGroup,
       "commonVarbindCompliance": commonVarbindCompliance}
)
