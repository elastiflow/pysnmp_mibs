# SNMP MIB module (CISCO-SNMP-HANDSHAKE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SNMP-HANDSHAKE-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:52:59 2025
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

(bsnWireless,) = mibBuilder.importSymbols(
    "AIRESPACE-WIRELESS-MIB",
    "bsnWireless")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSnmpHandshakeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 40)
)
if mibBuilder.loadTexts:
    ciscoSnmpHandshakeMIB.setRevisions(
        ("2007-05-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSnmpHandshakeMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSnmpHandshakeMIBNotifs = _CiscoSnmpHandshakeMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 40, 0)
)
_CiscoSnmpHandshakeMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSnmpHandshakeMIBObjects = _CiscoSnmpHandshakeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 40, 1)
)
_CiscoSnmpHandshakeProcess_ObjectIdentity = ObjectIdentity
ciscoSnmpHandshakeProcess = _CiscoSnmpHandshakeProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 1)
)


class _CsHandshakeInit_Type(OctetString):
    """Custom type csHandshakeInit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixedLength = 16


_CsHandshakeInit_Type.__name__ = "OctetString"
_CsHandshakeInit_Object = MibScalar
csHandshakeInit = _CsHandshakeInit_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 1, 1),
    _CsHandshakeInit_Type()
)
csHandshakeInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csHandshakeInit.setStatus("current")


class _CsHandshakeUpdate_Type(OctetString):
    """Custom type csHandshakeUpdate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixedLength = 16


_CsHandshakeUpdate_Type.__name__ = "OctetString"
_CsHandshakeUpdate_Object = MibScalar
csHandshakeUpdate = _CsHandshakeUpdate_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 1, 2),
    _CsHandshakeUpdate_Type()
)
csHandshakeUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csHandshakeUpdate.setStatus("current")
_CiscoSnmpHandshakeTest_ObjectIdentity = ObjectIdentity
ciscoSnmpHandshakeTest = _CiscoSnmpHandshakeTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 2)
)
_CsHandshakeCheck_Type = TruthValue
_CsHandshakeCheck_Object = MibScalar
csHandshakeCheck = _CsHandshakeCheck_Object(
    (1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 2, 1),
    _CsHandshakeCheck_Type()
)
csHandshakeCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csHandshakeCheck.setStatus("current")
_CiscoSnmpHandshakeMIBConform_ObjectIdentity = ObjectIdentity
ciscoSnmpHandshakeMIBConform = _CiscoSnmpHandshakeMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 40, 2)
)
_CiscoSnmpHandshakeMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSnmpHandshakeMIBCompliances = _CiscoSnmpHandshakeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 1)
)
_CiscoSnmpHandshakeMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSnmpHandshakeMIBGroups = _CiscoSnmpHandshakeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 2)
)

# Managed Objects groups

ciscoSnmpHandshakeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 2, 1)
)
ciscoSnmpHandshakeGroup.setObjects(
      *(("CISCO-SNMP-HANDSHAKE-MIB", "csHandshakeInit"),
        ("CISCO-SNMP-HANDSHAKE-MIB", "csHandshakeUpdate"),
        ("CISCO-SNMP-HANDSHAKE-MIB", "csHandshakeCheck"))
)
if mibBuilder.loadTexts:
    ciscoSnmpHandshakeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSnmpHandshakeMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 1, 1)
)
ciscoSnmpHandshakeMIBCompliance.setObjects(
    ("CISCO-SNMP-HANDSHAKE-MIB", "ciscoSnmpHandshakeGroup")
)
if mibBuilder.loadTexts:
    ciscoSnmpHandshakeMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SNMP-HANDSHAKE-MIB",
    **{"ciscoSnmpHandshakeMIB": ciscoSnmpHandshakeMIB,
       "ciscoSnmpHandshakeMIBNotifs": ciscoSnmpHandshakeMIBNotifs,
       "ciscoSnmpHandshakeMIBObjects": ciscoSnmpHandshakeMIBObjects,
       "ciscoSnmpHandshakeProcess": ciscoSnmpHandshakeProcess,
       "csHandshakeInit": csHandshakeInit,
       "csHandshakeUpdate": csHandshakeUpdate,
       "ciscoSnmpHandshakeTest": ciscoSnmpHandshakeTest,
       "csHandshakeCheck": csHandshakeCheck,
       "ciscoSnmpHandshakeMIBConform": ciscoSnmpHandshakeMIBConform,
       "ciscoSnmpHandshakeMIBCompliances": ciscoSnmpHandshakeMIBCompliances,
       "ciscoSnmpHandshakeMIBCompliance": ciscoSnmpHandshakeMIBCompliance,
       "ciscoSnmpHandshakeMIBGroups": ciscoSnmpHandshakeMIBGroups,
       "ciscoSnmpHandshakeGroup": ciscoSnmpHandshakeGroup}
)
