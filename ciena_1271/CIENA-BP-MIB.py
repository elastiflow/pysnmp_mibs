# SNMP MIB module (CIENA-BP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_1271/CIENA-BP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:39:45 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaBpNtfMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1393, 1)
)
if mibBuilder.loadTexts:
    cienaBpNtfMibModule.setRevisions(
        ("2016-04-22 20:55",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ciena_ObjectIdentity = ObjectIdentity
ciena = _Ciena_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271)
)
if mibBuilder.loadTexts:
    ciena.setStatus("current")
_CienaBpNtfMibModules_ObjectIdentity = ObjectIdentity
cienaBpNtfMibModules = _CienaBpNtfMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1393)
)
if mibBuilder.loadTexts:
    cienaBpNtfMibModules.setStatus("current")
_CienaBpNotification_ObjectIdentity = ObjectIdentity
cienaBpNotification = _CienaBpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1393, 1, 1)
)
_CienaBpNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaBpNotificationPrefix = _CienaBpNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1393, 1, 1, 1)
)
_CienaBpNotificationObjects_ObjectIdentity = ObjectIdentity
cienaBpNotificationObjects = _CienaBpNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 1393, 1, 1, 2)
)
_FieldTestRule1numericvalue_Type = Integer32
_FieldTestRule1numericvalue_Object = MibScalar
fieldTestRule1numericvalue = _FieldTestRule1numericvalue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1393, 1, 1, 2, 1),
    _FieldTestRule1numericvalue_Type()
)
fieldTestRule1numericvalue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fieldTestRule1numericvalue.setStatus("current")
_FieldTestRule1testname_Type = DisplayString
_FieldTestRule1testname_Object = MibScalar
fieldTestRule1testname = _FieldTestRule1testname_Object(
    (1, 3, 6, 1, 4, 1, 1271, 1393, 1, 1, 2, 2),
    _FieldTestRule1testname_Type()
)
fieldTestRule1testname.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fieldTestRule1testname.setStatus("current")

# Managed Objects groups


# Notification objects

ntf1TestRule1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 1393, 1, 1, 1, 1)
)
ntf1TestRule1.setObjects(
      *(("CIENA-BP-MIB", "fieldTestRule1numericvalue"),
        ("CIENA-BP-MIB", "fieldTestRule1testname"))
)
if mibBuilder.loadTexts:
    ntf1TestRule1.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-BP-MIB",
    **{"ciena": ciena,
       "cienaBpNtfMibModules": cienaBpNtfMibModules,
       "cienaBpNtfMibModule": cienaBpNtfMibModule,
       "cienaBpNotification": cienaBpNotification,
       "cienaBpNotificationPrefix": cienaBpNotificationPrefix,
       "ntf1TestRule1": ntf1TestRule1,
       "cienaBpNotificationObjects": cienaBpNotificationObjects,
       "fieldTestRule1numericvalue": fieldTestRule1numericvalue,
       "fieldTestRule1testname": fieldTestRule1testname}
)
