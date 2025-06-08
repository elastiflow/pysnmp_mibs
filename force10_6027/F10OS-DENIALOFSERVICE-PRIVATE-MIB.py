# SNMP MIB module (F10OS-DENIALOFSERVICE-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/force10_6027/F10OS-DENIALOFSERVICE-PRIVATE-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:18:09 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

sFTOSDenialOfService = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 31)
)
if mibBuilder.loadTexts:
    sFTOSDenialOfService.setRevisions(
        ("2005-02-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentSwitchDenialOfServiceGroup_ObjectIdentity = ObjectIdentity
agentSwitchDenialOfServiceGroup = _AgentSwitchDenialOfServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 31, 1)
)


class _AgentSwitchDenialOfServiceSIPDIPMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceSIPDIPMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceSIPDIPMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceSIPDIPMode_Object = MibScalar
agentSwitchDenialOfServiceSIPDIPMode = _AgentSwitchDenialOfServiceSIPDIPMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 31, 1, 1),
    _AgentSwitchDenialOfServiceSIPDIPMode_Type()
)
agentSwitchDenialOfServiceSIPDIPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceSIPDIPMode.setStatus("current")


class _AgentSwitchDenialOfServiceFirstFragMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceFirstFragMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceFirstFragMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceFirstFragMode_Object = MibScalar
agentSwitchDenialOfServiceFirstFragMode = _AgentSwitchDenialOfServiceFirstFragMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 31, 1, 2),
    _AgentSwitchDenialOfServiceFirstFragMode_Type()
)
agentSwitchDenialOfServiceFirstFragMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceFirstFragMode.setStatus("current")


class _AgentSwitchDenialOfServiceTCPHdrSize_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceTCPHdrSize based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentSwitchDenialOfServiceTCPHdrSize_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceTCPHdrSize_Object = MibScalar
agentSwitchDenialOfServiceTCPHdrSize = _AgentSwitchDenialOfServiceTCPHdrSize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 31, 1, 3),
    _AgentSwitchDenialOfServiceTCPHdrSize_Type()
)
agentSwitchDenialOfServiceTCPHdrSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceTCPHdrSize.setStatus("current")


class _AgentSwitchDenialOfServiceTCPFragMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceTCPFragMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceTCPFragMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceTCPFragMode_Object = MibScalar
agentSwitchDenialOfServiceTCPFragMode = _AgentSwitchDenialOfServiceTCPFragMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 31, 1, 4),
    _AgentSwitchDenialOfServiceTCPFragMode_Type()
)
agentSwitchDenialOfServiceTCPFragMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceTCPFragMode.setStatus("current")


class _AgentSwitchDenialOfServiceTCPFlagMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceTCPFlagMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceTCPFlagMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceTCPFlagMode_Object = MibScalar
agentSwitchDenialOfServiceTCPFlagMode = _AgentSwitchDenialOfServiceTCPFlagMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 31, 1, 5),
    _AgentSwitchDenialOfServiceTCPFlagMode_Type()
)
agentSwitchDenialOfServiceTCPFlagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceTCPFlagMode.setStatus("current")


class _AgentSwitchDenialOfServiceL4PortMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceL4PortMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceL4PortMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceL4PortMode_Object = MibScalar
agentSwitchDenialOfServiceL4PortMode = _AgentSwitchDenialOfServiceL4PortMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 31, 1, 6),
    _AgentSwitchDenialOfServiceL4PortMode_Type()
)
agentSwitchDenialOfServiceL4PortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceL4PortMode.setStatus("current")


class _AgentSwitchDenialOfServiceICMPMode_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceICMPMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchDenialOfServiceICMPMode_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceICMPMode_Object = MibScalar
agentSwitchDenialOfServiceICMPMode = _AgentSwitchDenialOfServiceICMPMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 31, 1, 7),
    _AgentSwitchDenialOfServiceICMPMode_Type()
)
agentSwitchDenialOfServiceICMPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceICMPMode.setStatus("current")


class _AgentSwitchDenialOfServiceICMPSize_Type(Integer32):
    """Custom type agentSwitchDenialOfServiceICMPSize based on Integer32"""
    defaultValue = 1023

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_AgentSwitchDenialOfServiceICMPSize_Type.__name__ = "Integer32"
_AgentSwitchDenialOfServiceICMPSize_Object = MibScalar
agentSwitchDenialOfServiceICMPSize = _AgentSwitchDenialOfServiceICMPSize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 31, 1, 8),
    _AgentSwitchDenialOfServiceICMPSize_Type()
)
agentSwitchDenialOfServiceICMPSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDenialOfServiceICMPSize.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10OS-DENIALOFSERVICE-PRIVATE-MIB",
    **{"sFTOSDenialOfService": sFTOSDenialOfService,
       "agentSwitchDenialOfServiceGroup": agentSwitchDenialOfServiceGroup,
       "agentSwitchDenialOfServiceSIPDIPMode": agentSwitchDenialOfServiceSIPDIPMode,
       "agentSwitchDenialOfServiceFirstFragMode": agentSwitchDenialOfServiceFirstFragMode,
       "agentSwitchDenialOfServiceTCPHdrSize": agentSwitchDenialOfServiceTCPHdrSize,
       "agentSwitchDenialOfServiceTCPFragMode": agentSwitchDenialOfServiceTCPFragMode,
       "agentSwitchDenialOfServiceTCPFlagMode": agentSwitchDenialOfServiceTCPFlagMode,
       "agentSwitchDenialOfServiceL4PortMode": agentSwitchDenialOfServiceL4PortMode,
       "agentSwitchDenialOfServiceICMPMode": agentSwitchDenialOfServiceICMPMode,
       "agentSwitchDenialOfServiceICMPSize": agentSwitchDenialOfServiceICMPSize}
)
