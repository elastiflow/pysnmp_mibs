# SNMP MIB module (SFTOS-MGMT-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/force10_6027/SFTOS-MGMT-SECURITY-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:18:01 2025
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

sFTOSMgmtSecurity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 11)
)
if mibBuilder.loadTexts:
    sFTOSMgmtSecurity.setRevisions(
        ("2005-01-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentSSLConfigGroup_ObjectIdentity = ObjectIdentity
agentSSLConfigGroup = _AgentSSLConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 11, 1)
)


class _AgentSSLAdminMode_Type(Integer32):
    """Custom type agentSSLAdminMode based on Integer32"""
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


_AgentSSLAdminMode_Type.__name__ = "Integer32"
_AgentSSLAdminMode_Object = MibScalar
agentSSLAdminMode = _AgentSSLAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 11, 1, 1),
    _AgentSSLAdminMode_Type()
)
agentSSLAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLAdminMode.setStatus("current")


class _AgentSSLSecurePort_Type(Integer32):
    """Custom type agentSSLSecurePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentSSLSecurePort_Type.__name__ = "Integer32"
_AgentSSLSecurePort_Object = MibScalar
agentSSLSecurePort = _AgentSSLSecurePort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 11, 1, 2),
    _AgentSSLSecurePort_Type()
)
agentSSLSecurePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLSecurePort.setStatus("current")


class _AgentSSLProtocolLevel_Type(Integer32):
    """Custom type agentSSLProtocolLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ssl30", 1),
          ("tls10", 2),
          ("both", 3))
    )


_AgentSSLProtocolLevel_Type.__name__ = "Integer32"
_AgentSSLProtocolLevel_Object = MibScalar
agentSSLProtocolLevel = _AgentSSLProtocolLevel_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 11, 1, 3),
    _AgentSSLProtocolLevel_Type()
)
agentSSLProtocolLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLProtocolLevel.setStatus("current")
_AgentSSHConfigGroup_ObjectIdentity = ObjectIdentity
agentSSHConfigGroup = _AgentSSHConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 11, 2)
)


class _AgentSSHAdminMode_Type(Integer32):
    """Custom type agentSSHAdminMode based on Integer32"""
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


_AgentSSHAdminMode_Type.__name__ = "Integer32"
_AgentSSHAdminMode_Object = MibScalar
agentSSHAdminMode = _AgentSSHAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 11, 2, 1),
    _AgentSSHAdminMode_Type()
)
agentSSHAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHAdminMode.setStatus("current")


class _AgentSSHProtocolLevel_Type(Integer32):
    """Custom type agentSSHProtocolLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ssh10", 1),
          ("ssh20", 2),
          ("both", 3))
    )


_AgentSSHProtocolLevel_Type.__name__ = "Integer32"
_AgentSSHProtocolLevel_Object = MibScalar
agentSSHProtocolLevel = _AgentSSHProtocolLevel_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 11, 2, 2),
    _AgentSSHProtocolLevel_Type()
)
agentSSHProtocolLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHProtocolLevel.setStatus("current")
_AgentSSHSessionsCount_Type = Integer32
_AgentSSHSessionsCount_Object = MibScalar
agentSSHSessionsCount = _AgentSSHSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 11, 2, 3),
    _AgentSSHSessionsCount_Type()
)
agentSSHSessionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSSHSessionsCount.setStatus("current")


class _AgentSSHMaxSessionsCount_Type(Integer32):
    """Custom type agentSSHMaxSessionsCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AgentSSHMaxSessionsCount_Type.__name__ = "Integer32"
_AgentSSHMaxSessionsCount_Object = MibScalar
agentSSHMaxSessionsCount = _AgentSSHMaxSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 11, 2, 4),
    _AgentSSHMaxSessionsCount_Type()
)
agentSSHMaxSessionsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHMaxSessionsCount.setStatus("current")


class _AgentSSHSessionTimeout_Type(Integer32):
    """Custom type agentSSHSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 160),
    )


_AgentSSHSessionTimeout_Type.__name__ = "Integer32"
_AgentSSHSessionTimeout_Object = MibScalar
agentSSHSessionTimeout = _AgentSSHSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 11, 2, 5),
    _AgentSSHSessionTimeout_Type()
)
agentSSHSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHSessionTimeout.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SFTOS-MGMT-SECURITY-MIB",
    **{"sFTOSMgmtSecurity": sFTOSMgmtSecurity,
       "agentSSLConfigGroup": agentSSLConfigGroup,
       "agentSSLAdminMode": agentSSLAdminMode,
       "agentSSLSecurePort": agentSSLSecurePort,
       "agentSSLProtocolLevel": agentSSLProtocolLevel,
       "agentSSHConfigGroup": agentSSHConfigGroup,
       "agentSSHAdminMode": agentSSHAdminMode,
       "agentSSHProtocolLevel": agentSSHProtocolLevel,
       "agentSSHSessionsCount": agentSSHSessionsCount,
       "agentSSHMaxSessionsCount": agentSSHMaxSessionsCount,
       "agentSSHSessionTimeout": agentSSHSessionTimeout}
)
