# SNMP MIB module (DNOS-DOT1X-AUTHENTICATION-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/dell_674/DNOS-DOT1X-AUTHENTICATION-SERVER-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:25:38 2025
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathdot1xAuthenticationServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 49)
)
if mibBuilder.loadTexts:
    fastPathdot1xAuthenticationServer.setRevisions(
        ("2011-01-26 00:00",
         "2009-11-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentDot1xAuthServUserConfigGroup_ObjectIdentity = ObjectIdentity
agentDot1xAuthServUserConfigGroup = _AgentDot1xAuthServUserConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 49, 1)
)


class _AgentDot1xAuthServUserConfigCreate_Type(DisplayString):
    """Custom type agentDot1xAuthServUserConfigCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AgentDot1xAuthServUserConfigCreate_Type.__name__ = "DisplayString"
_AgentDot1xAuthServUserConfigCreate_Object = MibScalar
agentDot1xAuthServUserConfigCreate = _AgentDot1xAuthServUserConfigCreate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 49, 1, 1),
    _AgentDot1xAuthServUserConfigCreate_Type()
)
agentDot1xAuthServUserConfigCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1xAuthServUserConfigCreate.setStatus("current")
_AgentDot1xAuthServUserConfigTable_Object = MibTable
agentDot1xAuthServUserConfigTable = _AgentDot1xAuthServUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 49, 1, 2)
)
if mibBuilder.loadTexts:
    agentDot1xAuthServUserConfigTable.setStatus("current")
_AgentDot1xAuthServUserConfigEntry_Object = MibTableRow
agentDot1xAuthServUserConfigEntry = _AgentDot1xAuthServUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 49, 1, 2, 1)
)
agentDot1xAuthServUserConfigEntry.setIndexNames(
    (0, "DNOS-DOT1X-AUTHENTICATION-SERVER-MIB", "agentDot1xAuthServUserIndex"),
)
if mibBuilder.loadTexts:
    agentDot1xAuthServUserConfigEntry.setStatus("current")


class _AgentDot1xAuthServUserIndex_Type(Integer32):
    """Custom type agentDot1xAuthServUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AgentDot1xAuthServUserIndex_Type.__name__ = "Integer32"
_AgentDot1xAuthServUserIndex_Object = MibTableColumn
agentDot1xAuthServUserIndex = _AgentDot1xAuthServUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 49, 1, 2, 1, 1),
    _AgentDot1xAuthServUserIndex_Type()
)
agentDot1xAuthServUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDot1xAuthServUserIndex.setStatus("current")


class _AgentDot1xAuthServUserName_Type(DisplayString):
    """Custom type agentDot1xAuthServUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AgentDot1xAuthServUserName_Type.__name__ = "DisplayString"
_AgentDot1xAuthServUserName_Object = MibTableColumn
agentDot1xAuthServUserName = _AgentDot1xAuthServUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 49, 1, 2, 1, 2),
    _AgentDot1xAuthServUserName_Type()
)
agentDot1xAuthServUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1xAuthServUserName.setStatus("current")


class _AgentDot1xAuthServUserPassword_Type(DisplayString):
    """Custom type agentDot1xAuthServUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentDot1xAuthServUserPassword_Type.__name__ = "DisplayString"
_AgentDot1xAuthServUserPassword_Object = MibTableColumn
agentDot1xAuthServUserPassword = _AgentDot1xAuthServUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 49, 1, 2, 1, 3),
    _AgentDot1xAuthServUserPassword_Type()
)
agentDot1xAuthServUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1xAuthServUserPassword.setStatus("current")
_AgentDot1xAuthServUserStatus_Type = RowStatus
_AgentDot1xAuthServUserStatus_Object = MibTableColumn
agentDot1xAuthServUserStatus = _AgentDot1xAuthServUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 49, 1, 2, 1, 4),
    _AgentDot1xAuthServUserStatus_Type()
)
agentDot1xAuthServUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1xAuthServUserStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-DOT1X-AUTHENTICATION-SERVER-MIB",
    **{"fastPathdot1xAuthenticationServer": fastPathdot1xAuthenticationServer,
       "agentDot1xAuthServUserConfigGroup": agentDot1xAuthServUserConfigGroup,
       "agentDot1xAuthServUserConfigCreate": agentDot1xAuthServUserConfigCreate,
       "agentDot1xAuthServUserConfigTable": agentDot1xAuthServUserConfigTable,
       "agentDot1xAuthServUserConfigEntry": agentDot1xAuthServUserConfigEntry,
       "agentDot1xAuthServUserIndex": agentDot1xAuthServUserIndex,
       "agentDot1xAuthServUserName": agentDot1xAuthServUserName,
       "agentDot1xAuthServUserPassword": agentDot1xAuthServUserPassword,
       "agentDot1xAuthServUserStatus": agentDot1xAuthServUserStatus}
)
