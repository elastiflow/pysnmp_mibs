# SNMP MIB module (TACACS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/force10_6027/TACACS-CLIENT-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:17:56 2025
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

(sFTOS,) = mibBuilder.importSymbols(
    "FORCE10-REF-MIB",
    "sFTOS")

(InetAddressIPv4,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

agentTacacsClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 18)
)
if mibBuilder.loadTexts:
    agentTacacsClientMIB.setRevisions(
        ("2005-02-18 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentTacacsClientObjects_ObjectIdentity = ObjectIdentity
agentTacacsClientObjects = _AgentTacacsClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 18, 1)
)
_AgentTacacsGlobalConfigGroup_ObjectIdentity = ObjectIdentity
agentTacacsGlobalConfigGroup = _AgentTacacsGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 18, 1, 1)
)


class _AgentTacacsGlobalTimeout_Type(Unsigned32):
    """Custom type agentTacacsGlobalTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AgentTacacsGlobalTimeout_Type.__name__ = "Unsigned32"
_AgentTacacsGlobalTimeout_Object = MibScalar
agentTacacsGlobalTimeout = _AgentTacacsGlobalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 18, 1, 1, 1),
    _AgentTacacsGlobalTimeout_Type()
)
agentTacacsGlobalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTacacsGlobalTimeout.setStatus("current")


class _AgentTacacsGlobalKey_Type(OctetString):
    """Custom type agentTacacsGlobalKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgentTacacsGlobalKey_Type.__name__ = "OctetString"
_AgentTacacsGlobalKey_Object = MibScalar
agentTacacsGlobalKey = _AgentTacacsGlobalKey_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 18, 1, 1, 2),
    _AgentTacacsGlobalKey_Type()
)
agentTacacsGlobalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTacacsGlobalKey.setStatus("current")
_AgentTacacsServerTable_Object = MibTable
agentTacacsServerTable = _AgentTacacsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 18, 1, 2)
)
if mibBuilder.loadTexts:
    agentTacacsServerTable.setStatus("current")
_AgentTacacsServerEntry_Object = MibTableRow
agentTacacsServerEntry = _AgentTacacsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 18, 1, 2, 1)
)
agentTacacsServerEntry.setIndexNames(
    (0, "TACACS-CLIENT-MIB", "agentTacacsServerIpAddress"),
)
if mibBuilder.loadTexts:
    agentTacacsServerEntry.setStatus("current")
_AgentTacacsServerIpAddress_Type = InetAddressIPv4
_AgentTacacsServerIpAddress_Object = MibTableColumn
agentTacacsServerIpAddress = _AgentTacacsServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 18, 1, 2, 1, 1),
    _AgentTacacsServerIpAddress_Type()
)
agentTacacsServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentTacacsServerIpAddress.setStatus("current")


class _AgentTacacsPortNumber_Type(Unsigned32):
    """Custom type agentTacacsPortNumber based on Unsigned32"""
    defaultValue = 49

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentTacacsPortNumber_Type.__name__ = "Unsigned32"
_AgentTacacsPortNumber_Object = MibTableColumn
agentTacacsPortNumber = _AgentTacacsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 18, 1, 2, 1, 2),
    _AgentTacacsPortNumber_Type()
)
agentTacacsPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTacacsPortNumber.setStatus("current")


class _AgentTacacsTimeOut_Type(Unsigned32):
    """Custom type agentTacacsTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AgentTacacsTimeOut_Type.__name__ = "Unsigned32"
_AgentTacacsTimeOut_Object = MibTableColumn
agentTacacsTimeOut = _AgentTacacsTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 18, 1, 2, 1, 3),
    _AgentTacacsTimeOut_Type()
)
agentTacacsTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTacacsTimeOut.setStatus("current")


class _AgentTacacsKey_Type(OctetString):
    """Custom type agentTacacsKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgentTacacsKey_Type.__name__ = "OctetString"
_AgentTacacsKey_Object = MibTableColumn
agentTacacsKey = _AgentTacacsKey_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 18, 1, 2, 1, 4),
    _AgentTacacsKey_Type()
)
agentTacacsKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTacacsKey.setStatus("current")


class _AgentTacacsPriority_Type(Unsigned32):
    """Custom type agentTacacsPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentTacacsPriority_Type.__name__ = "Unsigned32"
_AgentTacacsPriority_Object = MibTableColumn
agentTacacsPriority = _AgentTacacsPriority_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 18, 1, 2, 1, 5),
    _AgentTacacsPriority_Type()
)
agentTacacsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTacacsPriority.setStatus("current")
_AgentTacacsServerStatus_Type = RowStatus
_AgentTacacsServerStatus_Object = MibTableColumn
agentTacacsServerStatus = _AgentTacacsServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 18, 1, 2, 1, 6),
    _AgentTacacsServerStatus_Type()
)
agentTacacsServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTacacsServerStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TACACS-CLIENT-MIB",
    **{"agentTacacsClientMIB": agentTacacsClientMIB,
       "agentTacacsClientObjects": agentTacacsClientObjects,
       "agentTacacsGlobalConfigGroup": agentTacacsGlobalConfigGroup,
       "agentTacacsGlobalTimeout": agentTacacsGlobalTimeout,
       "agentTacacsGlobalKey": agentTacacsGlobalKey,
       "agentTacacsServerTable": agentTacacsServerTable,
       "agentTacacsServerEntry": agentTacacsServerEntry,
       "agentTacacsServerIpAddress": agentTacacsServerIpAddress,
       "agentTacacsPortNumber": agentTacacsPortNumber,
       "agentTacacsTimeOut": agentTacacsTimeOut,
       "agentTacacsKey": agentTacacsKey,
       "agentTacacsPriority": agentTacacsPriority,
       "agentTacacsServerStatus": agentTacacsServerStatus}
)
