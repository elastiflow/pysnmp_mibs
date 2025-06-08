# SNMP MIB module (RBN-CONFIG-ROLLBACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/RBN-CONFIG-ROLLBACK-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:52 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnPort,
 RbnSlot) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnPort",
    "RbnSlot")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbnConfigRollbackMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 105)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnConfigRollbackNotifications_ObjectIdentity = ObjectIdentity
rbnConfigRollbackNotifications = _RbnConfigRollbackNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 105, 0)
)
_RbnConfigRollbackObjects_ObjectIdentity = ObjectIdentity
rbnConfigRollbackObjects = _RbnConfigRollbackObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 105, 1)
)
_RbnConfigRollbackArchiveName_Type = SnmpAdminString
_RbnConfigRollbackArchiveName_Object = MibScalar
rbnConfigRollbackArchiveName = _RbnConfigRollbackArchiveName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 105, 1, 0),
    _RbnConfigRollbackArchiveName_Type()
)
rbnConfigRollbackArchiveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnConfigRollbackArchiveName.setStatus("current")
_RbnConfigRollbackUserName_Type = SnmpAdminString
_RbnConfigRollbackUserName_Object = MibScalar
rbnConfigRollbackUserName = _RbnConfigRollbackUserName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 105, 1, 1),
    _RbnConfigRollbackUserName_Type()
)
rbnConfigRollbackUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnConfigRollbackUserName.setStatus("current")
_RbnConfigRollbackTimeStamp_Type = DateAndTime
_RbnConfigRollbackTimeStamp_Object = MibScalar
rbnConfigRollbackTimeStamp = _RbnConfigRollbackTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 105, 1, 2),
    _RbnConfigRollbackTimeStamp_Type()
)
rbnConfigRollbackTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnConfigRollbackTimeStamp.setStatus("current")


class _RbnConfigRollbackAccessMethod_Type(Integer32):
    """Custom type rbnConfigRollbackAccessMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cli", 0),
          ("netconf", 1))
    )


_RbnConfigRollbackAccessMethod_Type.__name__ = "Integer32"
_RbnConfigRollbackAccessMethod_Object = MibScalar
rbnConfigRollbackAccessMethod = _RbnConfigRollbackAccessMethod_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 105, 1, 3),
    _RbnConfigRollbackAccessMethod_Type()
)
rbnConfigRollbackAccessMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnConfigRollbackAccessMethod.setStatus("current")
_RbnConfigRollbackIpAddress_Type = IpAddress
_RbnConfigRollbackIpAddress_Object = MibScalar
rbnConfigRollbackIpAddress = _RbnConfigRollbackIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 105, 1, 4),
    _RbnConfigRollbackIpAddress_Type()
)
rbnConfigRollbackIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnConfigRollbackIpAddress.setStatus("current")

# Managed Objects groups


# Notification objects

rbnConfigRollbackPerformedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 105, 0, 0)
)
rbnConfigRollbackPerformedEvent.setObjects(
      *(("RBN-CONFIG-ROLLBACK-MIB", "rbnConfigRollbackArchiveName"),
        ("RBN-CONFIG-ROLLBACK-MIB", "rbnConfigRollbackUserName"),
        ("RBN-CONFIG-ROLLBACK-MIB", "rbnConfigRollbackTimeStamp"),
        ("RBN-CONFIG-ROLLBACK-MIB", "rbnConfigRollbackAccessMethod"),
        ("RBN-CONFIG-ROLLBACK-MIB", "rbnConfigRollbackIpAddress"))
)
if mibBuilder.loadTexts:
    rbnConfigRollbackPerformedEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-CONFIG-ROLLBACK-MIB",
    **{"rbnConfigRollbackMIB": rbnConfigRollbackMIB,
       "rbnConfigRollbackNotifications": rbnConfigRollbackNotifications,
       "rbnConfigRollbackPerformedEvent": rbnConfigRollbackPerformedEvent,
       "rbnConfigRollbackObjects": rbnConfigRollbackObjects,
       "rbnConfigRollbackArchiveName": rbnConfigRollbackArchiveName,
       "rbnConfigRollbackUserName": rbnConfigRollbackUserName,
       "rbnConfigRollbackTimeStamp": rbnConfigRollbackTimeStamp,
       "rbnConfigRollbackAccessMethod": rbnConfigRollbackAccessMethod,
       "rbnConfigRollbackIpAddress": rbnConfigRollbackIpAddress}
)
