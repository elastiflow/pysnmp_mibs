# SNMP MIB module (ME1200-AUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-AUTH-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:30 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(ME1200DisplayString,
 ME1200Unsigned8) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200Unsigned8")

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

me1200AuthMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48)
)
if mibBuilder.loadTexts:
    me1200AuthMib.setRevisions(
        ("2014-04-07 00:00",
         "2014-03-07 00:00",
         "2014-02-18 00:00",
         "2014-02-10 00:00",
         "2014-01-29 00:00",
         "2014-01-24 00:00",
         "2014-01-22 00:00",
         "2013-11-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200AuthAcctMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tacacs", 3))
    )



class ME1200AuthAuthorMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tacacs", 3))
    )



class ME1200AuthMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("local", 1),
          ("radius", 2),
          ("tacacs", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200AuthObjects_ObjectIdentity = ObjectIdentity
me1200AuthObjects = _Me1200AuthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1)
)
_Me1200AuthConfig_ObjectIdentity = ObjectIdentity
me1200AuthConfig = _Me1200AuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2)
)
_Me1200AuthGlobals_ObjectIdentity = ObjectIdentity
me1200AuthGlobals = _Me1200AuthGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1)
)
_Me1200AuthAgents_ObjectIdentity = ObjectIdentity
me1200AuthAgents = _Me1200AuthAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1)
)
_Me1200AuthAgentConsole_ObjectIdentity = ObjectIdentity
me1200AuthAgentConsole = _Me1200AuthAgentConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 1)
)
_Me1200AuthAgentConsoleMethodsTable_Object = MibTable
me1200AuthAgentConsoleMethodsTable = _Me1200AuthAgentConsoleMethodsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    me1200AuthAgentConsoleMethodsTable.setStatus("current")
_Me1200AuthAgentConsoleMethodsEntry_Object = MibTableRow
me1200AuthAgentConsoleMethodsEntry = _Me1200AuthAgentConsoleMethodsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 1, 1, 1)
)
me1200AuthAgentConsoleMethodsEntry.setIndexNames(
    (0, "ME1200-AUTH-MIB", "me1200AuthAgentConsoleMethodsMetodIndex"),
)
if mibBuilder.loadTexts:
    me1200AuthAgentConsoleMethodsEntry.setStatus("current")


class _Me1200AuthAgentConsoleMethodsMetodIndex_Type(Integer32):
    """Custom type me1200AuthAgentConsoleMethodsMetodIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Me1200AuthAgentConsoleMethodsMetodIndex_Type.__name__ = "Integer32"
_Me1200AuthAgentConsoleMethodsMetodIndex_Object = MibTableColumn
me1200AuthAgentConsoleMethodsMetodIndex = _Me1200AuthAgentConsoleMethodsMetodIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 1, 1, 1, 1),
    _Me1200AuthAgentConsoleMethodsMetodIndex_Type()
)
me1200AuthAgentConsoleMethodsMetodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200AuthAgentConsoleMethodsMetodIndex.setStatus("current")
_Me1200AuthAgentConsoleMethodsMethod_Type = ME1200AuthMethod
_Me1200AuthAgentConsoleMethodsMethod_Object = MibTableColumn
me1200AuthAgentConsoleMethodsMethod = _Me1200AuthAgentConsoleMethodsMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 1, 1, 1, 2),
    _Me1200AuthAgentConsoleMethodsMethod_Type()
)
me1200AuthAgentConsoleMethodsMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentConsoleMethodsMethod.setStatus("current")
_Me1200AuthAgentTelnet_ObjectIdentity = ObjectIdentity
me1200AuthAgentTelnet = _Me1200AuthAgentTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 2)
)
_Me1200AuthAgentTelnetMethodsTable_Object = MibTable
me1200AuthAgentTelnetMethodsTable = _Me1200AuthAgentTelnetMethodsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    me1200AuthAgentTelnetMethodsTable.setStatus("current")
_Me1200AuthAgentTelnetMethodsEntry_Object = MibTableRow
me1200AuthAgentTelnetMethodsEntry = _Me1200AuthAgentTelnetMethodsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 2, 1, 1)
)
me1200AuthAgentTelnetMethodsEntry.setIndexNames(
    (0, "ME1200-AUTH-MIB", "me1200AuthAgentTelnetMethodsMetodIndex"),
)
if mibBuilder.loadTexts:
    me1200AuthAgentTelnetMethodsEntry.setStatus("current")


class _Me1200AuthAgentTelnetMethodsMetodIndex_Type(Integer32):
    """Custom type me1200AuthAgentTelnetMethodsMetodIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Me1200AuthAgentTelnetMethodsMetodIndex_Type.__name__ = "Integer32"
_Me1200AuthAgentTelnetMethodsMetodIndex_Object = MibTableColumn
me1200AuthAgentTelnetMethodsMetodIndex = _Me1200AuthAgentTelnetMethodsMetodIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 2, 1, 1, 1),
    _Me1200AuthAgentTelnetMethodsMetodIndex_Type()
)
me1200AuthAgentTelnetMethodsMetodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200AuthAgentTelnetMethodsMetodIndex.setStatus("current")
_Me1200AuthAgentTelnetMethodsMethod_Type = ME1200AuthMethod
_Me1200AuthAgentTelnetMethodsMethod_Object = MibTableColumn
me1200AuthAgentTelnetMethodsMethod = _Me1200AuthAgentTelnetMethodsMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 2, 1, 1, 2),
    _Me1200AuthAgentTelnetMethodsMethod_Type()
)
me1200AuthAgentTelnetMethodsMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentTelnetMethodsMethod.setStatus("current")
_Me1200AuthAgentSSH_ObjectIdentity = ObjectIdentity
me1200AuthAgentSSH = _Me1200AuthAgentSSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 3)
)
_Me1200AuthAgentSSHMethodsTable_Object = MibTable
me1200AuthAgentSSHMethodsTable = _Me1200AuthAgentSSHMethodsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    me1200AuthAgentSSHMethodsTable.setStatus("current")
_Me1200AuthAgentSSHMethodsEntry_Object = MibTableRow
me1200AuthAgentSSHMethodsEntry = _Me1200AuthAgentSSHMethodsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 3, 1, 1)
)
me1200AuthAgentSSHMethodsEntry.setIndexNames(
    (0, "ME1200-AUTH-MIB", "me1200AuthAgentSSHMethodsMetodIndex"),
)
if mibBuilder.loadTexts:
    me1200AuthAgentSSHMethodsEntry.setStatus("current")


class _Me1200AuthAgentSSHMethodsMetodIndex_Type(Integer32):
    """Custom type me1200AuthAgentSSHMethodsMetodIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Me1200AuthAgentSSHMethodsMetodIndex_Type.__name__ = "Integer32"
_Me1200AuthAgentSSHMethodsMetodIndex_Object = MibTableColumn
me1200AuthAgentSSHMethodsMetodIndex = _Me1200AuthAgentSSHMethodsMetodIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 3, 1, 1, 1),
    _Me1200AuthAgentSSHMethodsMetodIndex_Type()
)
me1200AuthAgentSSHMethodsMetodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200AuthAgentSSHMethodsMetodIndex.setStatus("current")
_Me1200AuthAgentSSHMethodsMethod_Type = ME1200AuthMethod
_Me1200AuthAgentSSHMethodsMethod_Object = MibTableColumn
me1200AuthAgentSSHMethodsMethod = _Me1200AuthAgentSSHMethodsMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 3, 1, 1, 2),
    _Me1200AuthAgentSSHMethodsMethod_Type()
)
me1200AuthAgentSSHMethodsMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentSSHMethodsMethod.setStatus("current")
_Me1200AuthAgentHTTP_ObjectIdentity = ObjectIdentity
me1200AuthAgentHTTP = _Me1200AuthAgentHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 4)
)
_Me1200AuthAgentHTTPMethodsTable_Object = MibTable
me1200AuthAgentHTTPMethodsTable = _Me1200AuthAgentHTTPMethodsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    me1200AuthAgentHTTPMethodsTable.setStatus("current")
_Me1200AuthAgentHTTPMethodsEntry_Object = MibTableRow
me1200AuthAgentHTTPMethodsEntry = _Me1200AuthAgentHTTPMethodsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 4, 1, 1)
)
me1200AuthAgentHTTPMethodsEntry.setIndexNames(
    (0, "ME1200-AUTH-MIB", "me1200AuthAgentHTTPMethodsMetodIndex"),
)
if mibBuilder.loadTexts:
    me1200AuthAgentHTTPMethodsEntry.setStatus("current")


class _Me1200AuthAgentHTTPMethodsMetodIndex_Type(Integer32):
    """Custom type me1200AuthAgentHTTPMethodsMetodIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Me1200AuthAgentHTTPMethodsMetodIndex_Type.__name__ = "Integer32"
_Me1200AuthAgentHTTPMethodsMetodIndex_Object = MibTableColumn
me1200AuthAgentHTTPMethodsMetodIndex = _Me1200AuthAgentHTTPMethodsMetodIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 4, 1, 1, 1),
    _Me1200AuthAgentHTTPMethodsMetodIndex_Type()
)
me1200AuthAgentHTTPMethodsMetodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200AuthAgentHTTPMethodsMetodIndex.setStatus("current")
_Me1200AuthAgentHTTPMethodsMethod_Type = ME1200AuthMethod
_Me1200AuthAgentHTTPMethodsMethod_Object = MibTableColumn
me1200AuthAgentHTTPMethodsMethod = _Me1200AuthAgentHTTPMethodsMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 4, 1, 1, 2),
    _Me1200AuthAgentHTTPMethodsMethod_Type()
)
me1200AuthAgentHTTPMethodsMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentHTTPMethodsMethod.setStatus("current")
_Me1200AuthAgentAuthorConsole_ObjectIdentity = ObjectIdentity
me1200AuthAgentAuthorConsole = _Me1200AuthAgentAuthorConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 11)
)
_Me1200AuthAgentAuthorConsoleMethod_Type = ME1200AuthAuthorMethod
_Me1200AuthAgentAuthorConsoleMethod_Object = MibScalar
me1200AuthAgentAuthorConsoleMethod = _Me1200AuthAgentAuthorConsoleMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 11, 1),
    _Me1200AuthAgentAuthorConsoleMethod_Type()
)
me1200AuthAgentAuthorConsoleMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAuthorConsoleMethod.setStatus("current")
_Me1200AuthAgentAuthorConsoleCmdEnable_Type = TruthValue
_Me1200AuthAgentAuthorConsoleCmdEnable_Object = MibScalar
me1200AuthAgentAuthorConsoleCmdEnable = _Me1200AuthAgentAuthorConsoleCmdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 11, 2),
    _Me1200AuthAgentAuthorConsoleCmdEnable_Type()
)
me1200AuthAgentAuthorConsoleCmdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAuthorConsoleCmdEnable.setStatus("current")
_Me1200AuthAgentAuthorConsoleCmdPrivLvl_Type = ME1200Unsigned8
_Me1200AuthAgentAuthorConsoleCmdPrivLvl_Object = MibScalar
me1200AuthAgentAuthorConsoleCmdPrivLvl = _Me1200AuthAgentAuthorConsoleCmdPrivLvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 11, 3),
    _Me1200AuthAgentAuthorConsoleCmdPrivLvl_Type()
)
me1200AuthAgentAuthorConsoleCmdPrivLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAuthorConsoleCmdPrivLvl.setStatus("current")
_Me1200AuthAgentAuthorConsoleCfgCmdEnable_Type = TruthValue
_Me1200AuthAgentAuthorConsoleCfgCmdEnable_Object = MibScalar
me1200AuthAgentAuthorConsoleCfgCmdEnable = _Me1200AuthAgentAuthorConsoleCfgCmdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 11, 4),
    _Me1200AuthAgentAuthorConsoleCfgCmdEnable_Type()
)
me1200AuthAgentAuthorConsoleCfgCmdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAuthorConsoleCfgCmdEnable.setStatus("current")
_Me1200AuthAgentAuthorTelnet_ObjectIdentity = ObjectIdentity
me1200AuthAgentAuthorTelnet = _Me1200AuthAgentAuthorTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 12)
)
_Me1200AuthAgentAuthorTelnetMethod_Type = ME1200AuthAuthorMethod
_Me1200AuthAgentAuthorTelnetMethod_Object = MibScalar
me1200AuthAgentAuthorTelnetMethod = _Me1200AuthAgentAuthorTelnetMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 12, 1),
    _Me1200AuthAgentAuthorTelnetMethod_Type()
)
me1200AuthAgentAuthorTelnetMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAuthorTelnetMethod.setStatus("current")
_Me1200AuthAgentAuthorTelnetCmdEnable_Type = TruthValue
_Me1200AuthAgentAuthorTelnetCmdEnable_Object = MibScalar
me1200AuthAgentAuthorTelnetCmdEnable = _Me1200AuthAgentAuthorTelnetCmdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 12, 2),
    _Me1200AuthAgentAuthorTelnetCmdEnable_Type()
)
me1200AuthAgentAuthorTelnetCmdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAuthorTelnetCmdEnable.setStatus("current")
_Me1200AuthAgentAuthorTelnetCmdPrivLvl_Type = ME1200Unsigned8
_Me1200AuthAgentAuthorTelnetCmdPrivLvl_Object = MibScalar
me1200AuthAgentAuthorTelnetCmdPrivLvl = _Me1200AuthAgentAuthorTelnetCmdPrivLvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 12, 3),
    _Me1200AuthAgentAuthorTelnetCmdPrivLvl_Type()
)
me1200AuthAgentAuthorTelnetCmdPrivLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAuthorTelnetCmdPrivLvl.setStatus("current")
_Me1200AuthAgentAuthorTelnetCfgCmdEnable_Type = TruthValue
_Me1200AuthAgentAuthorTelnetCfgCmdEnable_Object = MibScalar
me1200AuthAgentAuthorTelnetCfgCmdEnable = _Me1200AuthAgentAuthorTelnetCfgCmdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 12, 4),
    _Me1200AuthAgentAuthorTelnetCfgCmdEnable_Type()
)
me1200AuthAgentAuthorTelnetCfgCmdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAuthorTelnetCfgCmdEnable.setStatus("current")
_Me1200AuthAgentAuthorSSH_ObjectIdentity = ObjectIdentity
me1200AuthAgentAuthorSSH = _Me1200AuthAgentAuthorSSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 13)
)
_Me1200AuthAgentAuthorSSHMethod_Type = ME1200AuthAuthorMethod
_Me1200AuthAgentAuthorSSHMethod_Object = MibScalar
me1200AuthAgentAuthorSSHMethod = _Me1200AuthAgentAuthorSSHMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 13, 1),
    _Me1200AuthAgentAuthorSSHMethod_Type()
)
me1200AuthAgentAuthorSSHMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAuthorSSHMethod.setStatus("current")
_Me1200AuthAgentAuthorSSHCmdEnable_Type = TruthValue
_Me1200AuthAgentAuthorSSHCmdEnable_Object = MibScalar
me1200AuthAgentAuthorSSHCmdEnable = _Me1200AuthAgentAuthorSSHCmdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 13, 2),
    _Me1200AuthAgentAuthorSSHCmdEnable_Type()
)
me1200AuthAgentAuthorSSHCmdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAuthorSSHCmdEnable.setStatus("current")
_Me1200AuthAgentAuthorSSHCmdPrivLvl_Type = ME1200Unsigned8
_Me1200AuthAgentAuthorSSHCmdPrivLvl_Object = MibScalar
me1200AuthAgentAuthorSSHCmdPrivLvl = _Me1200AuthAgentAuthorSSHCmdPrivLvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 13, 3),
    _Me1200AuthAgentAuthorSSHCmdPrivLvl_Type()
)
me1200AuthAgentAuthorSSHCmdPrivLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAuthorSSHCmdPrivLvl.setStatus("current")
_Me1200AuthAgentAuthorSSHCfgCmdEnable_Type = TruthValue
_Me1200AuthAgentAuthorSSHCfgCmdEnable_Object = MibScalar
me1200AuthAgentAuthorSSHCfgCmdEnable = _Me1200AuthAgentAuthorSSHCfgCmdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 13, 4),
    _Me1200AuthAgentAuthorSSHCfgCmdEnable_Type()
)
me1200AuthAgentAuthorSSHCfgCmdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAuthorSSHCfgCmdEnable.setStatus("current")
_Me1200AuthAgentAcctConsole_ObjectIdentity = ObjectIdentity
me1200AuthAgentAcctConsole = _Me1200AuthAgentAcctConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 21)
)
_Me1200AuthAgentAcctConsoleMethod_Type = ME1200AuthAcctMethod
_Me1200AuthAgentAcctConsoleMethod_Object = MibScalar
me1200AuthAgentAcctConsoleMethod = _Me1200AuthAgentAcctConsoleMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 21, 1),
    _Me1200AuthAgentAcctConsoleMethod_Type()
)
me1200AuthAgentAcctConsoleMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAcctConsoleMethod.setStatus("current")
_Me1200AuthAgentAcctConsoleCmdEnable_Type = TruthValue
_Me1200AuthAgentAcctConsoleCmdEnable_Object = MibScalar
me1200AuthAgentAcctConsoleCmdEnable = _Me1200AuthAgentAcctConsoleCmdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 21, 2),
    _Me1200AuthAgentAcctConsoleCmdEnable_Type()
)
me1200AuthAgentAcctConsoleCmdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAcctConsoleCmdEnable.setStatus("current")
_Me1200AuthAgentAcctConsoleCmdPrivLvl_Type = ME1200Unsigned8
_Me1200AuthAgentAcctConsoleCmdPrivLvl_Object = MibScalar
me1200AuthAgentAcctConsoleCmdPrivLvl = _Me1200AuthAgentAcctConsoleCmdPrivLvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 21, 3),
    _Me1200AuthAgentAcctConsoleCmdPrivLvl_Type()
)
me1200AuthAgentAcctConsoleCmdPrivLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAcctConsoleCmdPrivLvl.setStatus("current")
_Me1200AuthAgentAcctConsoleExecEnable_Type = TruthValue
_Me1200AuthAgentAcctConsoleExecEnable_Object = MibScalar
me1200AuthAgentAcctConsoleExecEnable = _Me1200AuthAgentAcctConsoleExecEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 21, 4),
    _Me1200AuthAgentAcctConsoleExecEnable_Type()
)
me1200AuthAgentAcctConsoleExecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAcctConsoleExecEnable.setStatus("current")
_Me1200AuthAgentAcctTelnet_ObjectIdentity = ObjectIdentity
me1200AuthAgentAcctTelnet = _Me1200AuthAgentAcctTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 22)
)
_Me1200AuthAgentAcctTelnetMethod_Type = ME1200AuthAcctMethod
_Me1200AuthAgentAcctTelnetMethod_Object = MibScalar
me1200AuthAgentAcctTelnetMethod = _Me1200AuthAgentAcctTelnetMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 22, 1),
    _Me1200AuthAgentAcctTelnetMethod_Type()
)
me1200AuthAgentAcctTelnetMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAcctTelnetMethod.setStatus("current")
_Me1200AuthAgentAcctTelnetCmdEnable_Type = TruthValue
_Me1200AuthAgentAcctTelnetCmdEnable_Object = MibScalar
me1200AuthAgentAcctTelnetCmdEnable = _Me1200AuthAgentAcctTelnetCmdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 22, 2),
    _Me1200AuthAgentAcctTelnetCmdEnable_Type()
)
me1200AuthAgentAcctTelnetCmdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAcctTelnetCmdEnable.setStatus("current")
_Me1200AuthAgentAcctTelnetCmdPrivLvl_Type = ME1200Unsigned8
_Me1200AuthAgentAcctTelnetCmdPrivLvl_Object = MibScalar
me1200AuthAgentAcctTelnetCmdPrivLvl = _Me1200AuthAgentAcctTelnetCmdPrivLvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 22, 3),
    _Me1200AuthAgentAcctTelnetCmdPrivLvl_Type()
)
me1200AuthAgentAcctTelnetCmdPrivLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAcctTelnetCmdPrivLvl.setStatus("current")
_Me1200AuthAgentAcctTelnetExecEnable_Type = TruthValue
_Me1200AuthAgentAcctTelnetExecEnable_Object = MibScalar
me1200AuthAgentAcctTelnetExecEnable = _Me1200AuthAgentAcctTelnetExecEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 22, 4),
    _Me1200AuthAgentAcctTelnetExecEnable_Type()
)
me1200AuthAgentAcctTelnetExecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAcctTelnetExecEnable.setStatus("current")
_Me1200AuthAgentAcctSSH_ObjectIdentity = ObjectIdentity
me1200AuthAgentAcctSSH = _Me1200AuthAgentAcctSSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 23)
)
_Me1200AuthAgentAcctSSHMethod_Type = ME1200AuthAcctMethod
_Me1200AuthAgentAcctSSHMethod_Object = MibScalar
me1200AuthAgentAcctSSHMethod = _Me1200AuthAgentAcctSSHMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 23, 1),
    _Me1200AuthAgentAcctSSHMethod_Type()
)
me1200AuthAgentAcctSSHMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAcctSSHMethod.setStatus("current")
_Me1200AuthAgentAcctSSHCmdEnable_Type = TruthValue
_Me1200AuthAgentAcctSSHCmdEnable_Object = MibScalar
me1200AuthAgentAcctSSHCmdEnable = _Me1200AuthAgentAcctSSHCmdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 23, 2),
    _Me1200AuthAgentAcctSSHCmdEnable_Type()
)
me1200AuthAgentAcctSSHCmdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAcctSSHCmdEnable.setStatus("current")
_Me1200AuthAgentAcctSSHCmdPrivLvl_Type = ME1200Unsigned8
_Me1200AuthAgentAcctSSHCmdPrivLvl_Object = MibScalar
me1200AuthAgentAcctSSHCmdPrivLvl = _Me1200AuthAgentAcctSSHCmdPrivLvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 23, 3),
    _Me1200AuthAgentAcctSSHCmdPrivLvl_Type()
)
me1200AuthAgentAcctSSHCmdPrivLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAcctSSHCmdPrivLvl.setStatus("current")
_Me1200AuthAgentAcctSSHExecEnable_Type = TruthValue
_Me1200AuthAgentAcctSSHExecEnable_Object = MibScalar
me1200AuthAgentAcctSSHExecEnable = _Me1200AuthAgentAcctSSHExecEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 1, 23, 4),
    _Me1200AuthAgentAcctSSHExecEnable_Type()
)
me1200AuthAgentAcctSSHExecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthAgentAcctSSHExecEnable.setStatus("current")
_Me1200AuthRADIUS_ObjectIdentity = ObjectIdentity
me1200AuthRADIUS = _Me1200AuthRADIUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2)
)
_Me1200AuthRADIUSglobal_ObjectIdentity = ObjectIdentity
me1200AuthRADIUSglobal = _Me1200AuthRADIUSglobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 1)
)
_Me1200AuthRADIUSglobalTimeout_Type = Unsigned32
_Me1200AuthRADIUSglobalTimeout_Object = MibScalar
me1200AuthRADIUSglobalTimeout = _Me1200AuthRADIUSglobalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 1, 1),
    _Me1200AuthRADIUSglobalTimeout_Type()
)
me1200AuthRADIUSglobalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthRADIUSglobalTimeout.setStatus("current")
_Me1200AuthRADIUSglobalRetransmit_Type = Unsigned32
_Me1200AuthRADIUSglobalRetransmit_Object = MibScalar
me1200AuthRADIUSglobalRetransmit = _Me1200AuthRADIUSglobalRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 1, 2),
    _Me1200AuthRADIUSglobalRetransmit_Type()
)
me1200AuthRADIUSglobalRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthRADIUSglobalRetransmit.setStatus("current")
_Me1200AuthRADIUSglobalDeadtime_Type = Unsigned32
_Me1200AuthRADIUSglobalDeadtime_Object = MibScalar
me1200AuthRADIUSglobalDeadtime = _Me1200AuthRADIUSglobalDeadtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 1, 3),
    _Me1200AuthRADIUSglobalDeadtime_Type()
)
me1200AuthRADIUSglobalDeadtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthRADIUSglobalDeadtime.setStatus("current")


class _Me1200AuthRADIUSglobalKey_Type(ME1200DisplayString):
    """Custom type me1200AuthRADIUSglobalKey based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Me1200AuthRADIUSglobalKey_Type.__name__ = "ME1200DisplayString"
_Me1200AuthRADIUSglobalKey_Object = MibScalar
me1200AuthRADIUSglobalKey = _Me1200AuthRADIUSglobalKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 1, 4),
    _Me1200AuthRADIUSglobalKey_Type()
)
me1200AuthRADIUSglobalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthRADIUSglobalKey.setStatus("current")
_Me1200AuthRADIUSconfig_ObjectIdentity = ObjectIdentity
me1200AuthRADIUSconfig = _Me1200AuthRADIUSconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 2)
)
_Me1200AuthRADIUSconfigNasIpv4Enable_Type = TruthValue
_Me1200AuthRADIUSconfigNasIpv4Enable_Object = MibScalar
me1200AuthRADIUSconfigNasIpv4Enable = _Me1200AuthRADIUSconfigNasIpv4Enable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 2, 1),
    _Me1200AuthRADIUSconfigNasIpv4Enable_Type()
)
me1200AuthRADIUSconfigNasIpv4Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthRADIUSconfigNasIpv4Enable.setStatus("current")
_Me1200AuthRADIUSconfigNasIpv4Address_Type = IpAddress
_Me1200AuthRADIUSconfigNasIpv4Address_Object = MibScalar
me1200AuthRADIUSconfigNasIpv4Address = _Me1200AuthRADIUSconfigNasIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 2, 2),
    _Me1200AuthRADIUSconfigNasIpv4Address_Type()
)
me1200AuthRADIUSconfigNasIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthRADIUSconfigNasIpv4Address.setStatus("current")
_Me1200AuthRADIUSconfigNasIpv6Enable_Type = TruthValue
_Me1200AuthRADIUSconfigNasIpv6Enable_Object = MibScalar
me1200AuthRADIUSconfigNasIpv6Enable = _Me1200AuthRADIUSconfigNasIpv6Enable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 2, 3),
    _Me1200AuthRADIUSconfigNasIpv6Enable_Type()
)
me1200AuthRADIUSconfigNasIpv6Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthRADIUSconfigNasIpv6Enable.setStatus("current")
_Me1200AuthRADIUSconfigNasIpv6Address_Type = InetAddressIPv6
_Me1200AuthRADIUSconfigNasIpv6Address_Object = MibScalar
me1200AuthRADIUSconfigNasIpv6Address = _Me1200AuthRADIUSconfigNasIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 2, 4),
    _Me1200AuthRADIUSconfigNasIpv6Address_Type()
)
me1200AuthRADIUSconfigNasIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthRADIUSconfigNasIpv6Address.setStatus("current")


class _Me1200AuthRADIUSconfigNasIdentifier_Type(ME1200DisplayString):
    """Custom type me1200AuthRADIUSconfigNasIdentifier based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Me1200AuthRADIUSconfigNasIdentifier_Type.__name__ = "ME1200DisplayString"
_Me1200AuthRADIUSconfigNasIdentifier_Object = MibScalar
me1200AuthRADIUSconfigNasIdentifier = _Me1200AuthRADIUSconfigNasIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 2, 5),
    _Me1200AuthRADIUSconfigNasIdentifier_Type()
)
me1200AuthRADIUSconfigNasIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthRADIUSconfigNasIdentifier.setStatus("current")
_Me1200AuthRADIUShostTable_Object = MibTable
me1200AuthRADIUShostTable = _Me1200AuthRADIUShostTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    me1200AuthRADIUShostTable.setStatus("current")
_Me1200AuthRADIUShostEntry_Object = MibTableRow
me1200AuthRADIUShostEntry = _Me1200AuthRADIUShostEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 3, 1)
)
me1200AuthRADIUShostEntry.setIndexNames(
    (0, "ME1200-AUTH-MIB", "me1200AuthRADIUShostIndex"),
)
if mibBuilder.loadTexts:
    me1200AuthRADIUShostEntry.setStatus("current")


class _Me1200AuthRADIUShostIndex_Type(Integer32):
    """Custom type me1200AuthRADIUShostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200AuthRADIUShostIndex_Type.__name__ = "Integer32"
_Me1200AuthRADIUShostIndex_Object = MibTableColumn
me1200AuthRADIUShostIndex = _Me1200AuthRADIUShostIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 3, 1, 1),
    _Me1200AuthRADIUShostIndex_Type()
)
me1200AuthRADIUShostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200AuthRADIUShostIndex.setStatus("current")


class _Me1200AuthRADIUShostAddress_Type(ME1200DisplayString):
    """Custom type me1200AuthRADIUShostAddress based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Me1200AuthRADIUShostAddress_Type.__name__ = "ME1200DisplayString"
_Me1200AuthRADIUShostAddress_Object = MibTableColumn
me1200AuthRADIUShostAddress = _Me1200AuthRADIUShostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 3, 1, 2),
    _Me1200AuthRADIUShostAddress_Type()
)
me1200AuthRADIUShostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthRADIUShostAddress.setStatus("current")
_Me1200AuthRADIUShostAuthPort_Type = Unsigned32
_Me1200AuthRADIUShostAuthPort_Object = MibTableColumn
me1200AuthRADIUShostAuthPort = _Me1200AuthRADIUShostAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 3, 1, 3),
    _Me1200AuthRADIUShostAuthPort_Type()
)
me1200AuthRADIUShostAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthRADIUShostAuthPort.setStatus("current")
_Me1200AuthRADIUShostAcctPort_Type = Unsigned32
_Me1200AuthRADIUShostAcctPort_Object = MibTableColumn
me1200AuthRADIUShostAcctPort = _Me1200AuthRADIUShostAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 3, 1, 4),
    _Me1200AuthRADIUShostAcctPort_Type()
)
me1200AuthRADIUShostAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthRADIUShostAcctPort.setStatus("current")
_Me1200AuthRADIUShostTimeout_Type = Unsigned32
_Me1200AuthRADIUShostTimeout_Object = MibTableColumn
me1200AuthRADIUShostTimeout = _Me1200AuthRADIUShostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 3, 1, 5),
    _Me1200AuthRADIUShostTimeout_Type()
)
me1200AuthRADIUShostTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthRADIUShostTimeout.setStatus("current")
_Me1200AuthRADIUShostRetransmit_Type = Unsigned32
_Me1200AuthRADIUShostRetransmit_Object = MibTableColumn
me1200AuthRADIUShostRetransmit = _Me1200AuthRADIUShostRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 3, 1, 6),
    _Me1200AuthRADIUShostRetransmit_Type()
)
me1200AuthRADIUShostRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthRADIUShostRetransmit.setStatus("current")


class _Me1200AuthRADIUShostKey_Type(ME1200DisplayString):
    """Custom type me1200AuthRADIUShostKey based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Me1200AuthRADIUShostKey_Type.__name__ = "ME1200DisplayString"
_Me1200AuthRADIUShostKey_Object = MibTableColumn
me1200AuthRADIUShostKey = _Me1200AuthRADIUShostKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 2, 3, 1, 7),
    _Me1200AuthRADIUShostKey_Type()
)
me1200AuthRADIUShostKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthRADIUShostKey.setStatus("current")
_Me1200AuthTACACS_ObjectIdentity = ObjectIdentity
me1200AuthTACACS = _Me1200AuthTACACS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 3)
)
_Me1200AuthTACACSglobal_ObjectIdentity = ObjectIdentity
me1200AuthTACACSglobal = _Me1200AuthTACACSglobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 3, 1)
)
_Me1200AuthTACACSglobalTimeout_Type = Unsigned32
_Me1200AuthTACACSglobalTimeout_Object = MibScalar
me1200AuthTACACSglobalTimeout = _Me1200AuthTACACSglobalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 3, 1, 1),
    _Me1200AuthTACACSglobalTimeout_Type()
)
me1200AuthTACACSglobalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthTACACSglobalTimeout.setStatus("current")
_Me1200AuthTACACSglobalDeadtime_Type = Unsigned32
_Me1200AuthTACACSglobalDeadtime_Object = MibScalar
me1200AuthTACACSglobalDeadtime = _Me1200AuthTACACSglobalDeadtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 3, 1, 2),
    _Me1200AuthTACACSglobalDeadtime_Type()
)
me1200AuthTACACSglobalDeadtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthTACACSglobalDeadtime.setStatus("current")


class _Me1200AuthTACACSglobalKey_Type(ME1200DisplayString):
    """Custom type me1200AuthTACACSglobalKey based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Me1200AuthTACACSglobalKey_Type.__name__ = "ME1200DisplayString"
_Me1200AuthTACACSglobalKey_Object = MibScalar
me1200AuthTACACSglobalKey = _Me1200AuthTACACSglobalKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 3, 1, 3),
    _Me1200AuthTACACSglobalKey_Type()
)
me1200AuthTACACSglobalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthTACACSglobalKey.setStatus("current")
_Me1200AuthTACACShostTable_Object = MibTable
me1200AuthTACACShostTable = _Me1200AuthTACACShostTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    me1200AuthTACACShostTable.setStatus("current")
_Me1200AuthTACACShostEntry_Object = MibTableRow
me1200AuthTACACShostEntry = _Me1200AuthTACACShostEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 3, 2, 1)
)
me1200AuthTACACShostEntry.setIndexNames(
    (0, "ME1200-AUTH-MIB", "me1200AuthTACACShostIndex"),
)
if mibBuilder.loadTexts:
    me1200AuthTACACShostEntry.setStatus("current")


class _Me1200AuthTACACShostIndex_Type(Integer32):
    """Custom type me1200AuthTACACShostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Me1200AuthTACACShostIndex_Type.__name__ = "Integer32"
_Me1200AuthTACACShostIndex_Object = MibTableColumn
me1200AuthTACACShostIndex = _Me1200AuthTACACShostIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 3, 2, 1, 1),
    _Me1200AuthTACACShostIndex_Type()
)
me1200AuthTACACShostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200AuthTACACShostIndex.setStatus("current")


class _Me1200AuthTACACShostAddress_Type(ME1200DisplayString):
    """Custom type me1200AuthTACACShostAddress based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Me1200AuthTACACShostAddress_Type.__name__ = "ME1200DisplayString"
_Me1200AuthTACACShostAddress_Object = MibTableColumn
me1200AuthTACACShostAddress = _Me1200AuthTACACShostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 3, 2, 1, 2),
    _Me1200AuthTACACShostAddress_Type()
)
me1200AuthTACACShostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthTACACShostAddress.setStatus("current")
_Me1200AuthTACACShostAuthPort_Type = Unsigned32
_Me1200AuthTACACShostAuthPort_Object = MibTableColumn
me1200AuthTACACShostAuthPort = _Me1200AuthTACACShostAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 3, 2, 1, 3),
    _Me1200AuthTACACShostAuthPort_Type()
)
me1200AuthTACACShostAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthTACACShostAuthPort.setStatus("current")
_Me1200AuthTACACShostTimeout_Type = Unsigned32
_Me1200AuthTACACShostTimeout_Object = MibTableColumn
me1200AuthTACACShostTimeout = _Me1200AuthTACACShostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 3, 2, 1, 4),
    _Me1200AuthTACACShostTimeout_Type()
)
me1200AuthTACACShostTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthTACACShostTimeout.setStatus("current")


class _Me1200AuthTACACShostKey_Type(ME1200DisplayString):
    """Custom type me1200AuthTACACShostKey based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Me1200AuthTACACShostKey_Type.__name__ = "ME1200DisplayString"
_Me1200AuthTACACShostKey_Object = MibTableColumn
me1200AuthTACACShostKey = _Me1200AuthTACACShostKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 1, 2, 1, 3, 2, 1, 5),
    _Me1200AuthTACACShostKey_Type()
)
me1200AuthTACACShostKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200AuthTACACShostKey.setStatus("current")
_Me1200AuthMibConformance_ObjectIdentity = ObjectIdentity
me1200AuthMibConformance = _Me1200AuthMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2)
)
_Me1200AuthMibCompliances_ObjectIdentity = ObjectIdentity
me1200AuthMibCompliances = _Me1200AuthMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 1)
)
_Me1200AuthMibGroups_ObjectIdentity = ObjectIdentity
me1200AuthMibGroups = _Me1200AuthMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 2)
)

# Managed Objects groups

me1200AuthAgentConsoleMethodsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 2, 1)
)
me1200AuthAgentConsoleMethodsTableInfoGroup.setObjects(
    ("ME1200-AUTH-MIB", "me1200AuthAgentConsoleMethodsMethod")
)
if mibBuilder.loadTexts:
    me1200AuthAgentConsoleMethodsTableInfoGroup.setStatus("current")

me1200AuthAgentTelnetMethodsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 2, 2)
)
me1200AuthAgentTelnetMethodsTableInfoGroup.setObjects(
    ("ME1200-AUTH-MIB", "me1200AuthAgentTelnetMethodsMethod")
)
if mibBuilder.loadTexts:
    me1200AuthAgentTelnetMethodsTableInfoGroup.setStatus("current")

me1200AuthAgentSSHMethodsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 2, 3)
)
me1200AuthAgentSSHMethodsTableInfoGroup.setObjects(
    ("ME1200-AUTH-MIB", "me1200AuthAgentSSHMethodsMethod")
)
if mibBuilder.loadTexts:
    me1200AuthAgentSSHMethodsTableInfoGroup.setStatus("current")

me1200AuthAgentHTTPMethodsTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 2, 4)
)
me1200AuthAgentHTTPMethodsTableInfoGroup.setObjects(
    ("ME1200-AUTH-MIB", "me1200AuthAgentHTTPMethodsMethod")
)
if mibBuilder.loadTexts:
    me1200AuthAgentHTTPMethodsTableInfoGroup.setStatus("current")

me1200AuthAgentAuthorConsoleInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 2, 5)
)
me1200AuthAgentAuthorConsoleInfoGroup.setObjects(
      *(("ME1200-AUTH-MIB", "me1200AuthAgentAuthorConsoleMethod"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAuthorConsoleCmdEnable"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAuthorConsoleCmdPrivLvl"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAuthorConsoleCfgCmdEnable"))
)
if mibBuilder.loadTexts:
    me1200AuthAgentAuthorConsoleInfoGroup.setStatus("current")

me1200AuthAgentAuthorTelnetInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 2, 6)
)
me1200AuthAgentAuthorTelnetInfoGroup.setObjects(
      *(("ME1200-AUTH-MIB", "me1200AuthAgentAuthorTelnetMethod"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAuthorTelnetCmdEnable"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAuthorTelnetCmdPrivLvl"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAuthorTelnetCfgCmdEnable"))
)
if mibBuilder.loadTexts:
    me1200AuthAgentAuthorTelnetInfoGroup.setStatus("current")

me1200AuthAgentAuthorSSHInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 2, 7)
)
me1200AuthAgentAuthorSSHInfoGroup.setObjects(
      *(("ME1200-AUTH-MIB", "me1200AuthAgentAuthorSSHMethod"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAuthorSSHCmdEnable"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAuthorSSHCmdPrivLvl"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAuthorSSHCfgCmdEnable"))
)
if mibBuilder.loadTexts:
    me1200AuthAgentAuthorSSHInfoGroup.setStatus("current")

me1200AuthAgentAcctConsoleInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 2, 8)
)
me1200AuthAgentAcctConsoleInfoGroup.setObjects(
      *(("ME1200-AUTH-MIB", "me1200AuthAgentAcctConsoleMethod"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAcctConsoleCmdEnable"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAcctConsoleCmdPrivLvl"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAcctConsoleExecEnable"))
)
if mibBuilder.loadTexts:
    me1200AuthAgentAcctConsoleInfoGroup.setStatus("current")

me1200AuthAgentAcctTelnetInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 2, 9)
)
me1200AuthAgentAcctTelnetInfoGroup.setObjects(
      *(("ME1200-AUTH-MIB", "me1200AuthAgentAcctTelnetMethod"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAcctTelnetCmdEnable"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAcctTelnetCmdPrivLvl"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAcctTelnetExecEnable"))
)
if mibBuilder.loadTexts:
    me1200AuthAgentAcctTelnetInfoGroup.setStatus("current")

me1200AuthAgentAcctSSHInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 2, 10)
)
me1200AuthAgentAcctSSHInfoGroup.setObjects(
      *(("ME1200-AUTH-MIB", "me1200AuthAgentAcctSSHMethod"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAcctSSHCmdEnable"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAcctSSHCmdPrivLvl"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAcctSSHExecEnable"))
)
if mibBuilder.loadTexts:
    me1200AuthAgentAcctSSHInfoGroup.setStatus("current")

me1200AuthRADIUSglobalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 2, 11)
)
me1200AuthRADIUSglobalInfoGroup.setObjects(
      *(("ME1200-AUTH-MIB", "me1200AuthRADIUSglobalTimeout"),
        ("ME1200-AUTH-MIB", "me1200AuthRADIUSglobalRetransmit"),
        ("ME1200-AUTH-MIB", "me1200AuthRADIUSglobalDeadtime"),
        ("ME1200-AUTH-MIB", "me1200AuthRADIUSglobalKey"))
)
if mibBuilder.loadTexts:
    me1200AuthRADIUSglobalInfoGroup.setStatus("current")

me1200AuthRADIUSconfigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 2, 12)
)
me1200AuthRADIUSconfigInfoGroup.setObjects(
      *(("ME1200-AUTH-MIB", "me1200AuthRADIUSconfigNasIpv4Enable"),
        ("ME1200-AUTH-MIB", "me1200AuthRADIUSconfigNasIpv4Address"),
        ("ME1200-AUTH-MIB", "me1200AuthRADIUSconfigNasIpv6Enable"),
        ("ME1200-AUTH-MIB", "me1200AuthRADIUSconfigNasIpv6Address"),
        ("ME1200-AUTH-MIB", "me1200AuthRADIUSconfigNasIdentifier"))
)
if mibBuilder.loadTexts:
    me1200AuthRADIUSconfigInfoGroup.setStatus("current")

me1200AuthRADIUShostTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 2, 13)
)
me1200AuthRADIUShostTableInfoGroup.setObjects(
      *(("ME1200-AUTH-MIB", "me1200AuthRADIUShostAddress"),
        ("ME1200-AUTH-MIB", "me1200AuthRADIUShostAuthPort"),
        ("ME1200-AUTH-MIB", "me1200AuthRADIUShostAcctPort"),
        ("ME1200-AUTH-MIB", "me1200AuthRADIUShostTimeout"),
        ("ME1200-AUTH-MIB", "me1200AuthRADIUShostRetransmit"),
        ("ME1200-AUTH-MIB", "me1200AuthRADIUShostKey"))
)
if mibBuilder.loadTexts:
    me1200AuthRADIUShostTableInfoGroup.setStatus("current")

me1200AuthTACACSglobalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 2, 14)
)
me1200AuthTACACSglobalInfoGroup.setObjects(
      *(("ME1200-AUTH-MIB", "me1200AuthTACACSglobalTimeout"),
        ("ME1200-AUTH-MIB", "me1200AuthTACACSglobalDeadtime"),
        ("ME1200-AUTH-MIB", "me1200AuthTACACSglobalKey"))
)
if mibBuilder.loadTexts:
    me1200AuthTACACSglobalInfoGroup.setStatus("current")

me1200AuthTACACShostTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 2, 15)
)
me1200AuthTACACShostTableInfoGroup.setObjects(
      *(("ME1200-AUTH-MIB", "me1200AuthTACACShostAddress"),
        ("ME1200-AUTH-MIB", "me1200AuthTACACShostAuthPort"),
        ("ME1200-AUTH-MIB", "me1200AuthTACACShostTimeout"),
        ("ME1200-AUTH-MIB", "me1200AuthTACACShostKey"))
)
if mibBuilder.loadTexts:
    me1200AuthTACACShostTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200AuthMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 48, 2, 1, 1)
)
me1200AuthMibCompliance.setObjects(
      *(("ME1200-AUTH-MIB", "me1200AuthAgentConsoleMethodsTableInfoGroup"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentTelnetMethodsTableInfoGroup"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentSSHMethodsTableInfoGroup"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentHTTPMethodsTableInfoGroup"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAuthorConsoleInfoGroup"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAuthorTelnetInfoGroup"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAuthorSSHInfoGroup"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAcctConsoleInfoGroup"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAcctTelnetInfoGroup"),
        ("ME1200-AUTH-MIB", "me1200AuthAgentAcctSSHInfoGroup"),
        ("ME1200-AUTH-MIB", "me1200AuthRADIUSglobalInfoGroup"),
        ("ME1200-AUTH-MIB", "me1200AuthRADIUSconfigInfoGroup"),
        ("ME1200-AUTH-MIB", "me1200AuthRADIUShostTableInfoGroup"),
        ("ME1200-AUTH-MIB", "me1200AuthTACACSglobalInfoGroup"),
        ("ME1200-AUTH-MIB", "me1200AuthTACACShostTableInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200AuthMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-AUTH-MIB",
    **{"ME1200AuthAcctMethod": ME1200AuthAcctMethod,
       "ME1200AuthAuthorMethod": ME1200AuthAuthorMethod,
       "ME1200AuthMethod": ME1200AuthMethod,
       "me1200AuthMib": me1200AuthMib,
       "me1200AuthObjects": me1200AuthObjects,
       "me1200AuthConfig": me1200AuthConfig,
       "me1200AuthGlobals": me1200AuthGlobals,
       "me1200AuthAgents": me1200AuthAgents,
       "me1200AuthAgentConsole": me1200AuthAgentConsole,
       "me1200AuthAgentConsoleMethodsTable": me1200AuthAgentConsoleMethodsTable,
       "me1200AuthAgentConsoleMethodsEntry": me1200AuthAgentConsoleMethodsEntry,
       "me1200AuthAgentConsoleMethodsMetodIndex": me1200AuthAgentConsoleMethodsMetodIndex,
       "me1200AuthAgentConsoleMethodsMethod": me1200AuthAgentConsoleMethodsMethod,
       "me1200AuthAgentTelnet": me1200AuthAgentTelnet,
       "me1200AuthAgentTelnetMethodsTable": me1200AuthAgentTelnetMethodsTable,
       "me1200AuthAgentTelnetMethodsEntry": me1200AuthAgentTelnetMethodsEntry,
       "me1200AuthAgentTelnetMethodsMetodIndex": me1200AuthAgentTelnetMethodsMetodIndex,
       "me1200AuthAgentTelnetMethodsMethod": me1200AuthAgentTelnetMethodsMethod,
       "me1200AuthAgentSSH": me1200AuthAgentSSH,
       "me1200AuthAgentSSHMethodsTable": me1200AuthAgentSSHMethodsTable,
       "me1200AuthAgentSSHMethodsEntry": me1200AuthAgentSSHMethodsEntry,
       "me1200AuthAgentSSHMethodsMetodIndex": me1200AuthAgentSSHMethodsMetodIndex,
       "me1200AuthAgentSSHMethodsMethod": me1200AuthAgentSSHMethodsMethod,
       "me1200AuthAgentHTTP": me1200AuthAgentHTTP,
       "me1200AuthAgentHTTPMethodsTable": me1200AuthAgentHTTPMethodsTable,
       "me1200AuthAgentHTTPMethodsEntry": me1200AuthAgentHTTPMethodsEntry,
       "me1200AuthAgentHTTPMethodsMetodIndex": me1200AuthAgentHTTPMethodsMetodIndex,
       "me1200AuthAgentHTTPMethodsMethod": me1200AuthAgentHTTPMethodsMethod,
       "me1200AuthAgentAuthorConsole": me1200AuthAgentAuthorConsole,
       "me1200AuthAgentAuthorConsoleMethod": me1200AuthAgentAuthorConsoleMethod,
       "me1200AuthAgentAuthorConsoleCmdEnable": me1200AuthAgentAuthorConsoleCmdEnable,
       "me1200AuthAgentAuthorConsoleCmdPrivLvl": me1200AuthAgentAuthorConsoleCmdPrivLvl,
       "me1200AuthAgentAuthorConsoleCfgCmdEnable": me1200AuthAgentAuthorConsoleCfgCmdEnable,
       "me1200AuthAgentAuthorTelnet": me1200AuthAgentAuthorTelnet,
       "me1200AuthAgentAuthorTelnetMethod": me1200AuthAgentAuthorTelnetMethod,
       "me1200AuthAgentAuthorTelnetCmdEnable": me1200AuthAgentAuthorTelnetCmdEnable,
       "me1200AuthAgentAuthorTelnetCmdPrivLvl": me1200AuthAgentAuthorTelnetCmdPrivLvl,
       "me1200AuthAgentAuthorTelnetCfgCmdEnable": me1200AuthAgentAuthorTelnetCfgCmdEnable,
       "me1200AuthAgentAuthorSSH": me1200AuthAgentAuthorSSH,
       "me1200AuthAgentAuthorSSHMethod": me1200AuthAgentAuthorSSHMethod,
       "me1200AuthAgentAuthorSSHCmdEnable": me1200AuthAgentAuthorSSHCmdEnable,
       "me1200AuthAgentAuthorSSHCmdPrivLvl": me1200AuthAgentAuthorSSHCmdPrivLvl,
       "me1200AuthAgentAuthorSSHCfgCmdEnable": me1200AuthAgentAuthorSSHCfgCmdEnable,
       "me1200AuthAgentAcctConsole": me1200AuthAgentAcctConsole,
       "me1200AuthAgentAcctConsoleMethod": me1200AuthAgentAcctConsoleMethod,
       "me1200AuthAgentAcctConsoleCmdEnable": me1200AuthAgentAcctConsoleCmdEnable,
       "me1200AuthAgentAcctConsoleCmdPrivLvl": me1200AuthAgentAcctConsoleCmdPrivLvl,
       "me1200AuthAgentAcctConsoleExecEnable": me1200AuthAgentAcctConsoleExecEnable,
       "me1200AuthAgentAcctTelnet": me1200AuthAgentAcctTelnet,
       "me1200AuthAgentAcctTelnetMethod": me1200AuthAgentAcctTelnetMethod,
       "me1200AuthAgentAcctTelnetCmdEnable": me1200AuthAgentAcctTelnetCmdEnable,
       "me1200AuthAgentAcctTelnetCmdPrivLvl": me1200AuthAgentAcctTelnetCmdPrivLvl,
       "me1200AuthAgentAcctTelnetExecEnable": me1200AuthAgentAcctTelnetExecEnable,
       "me1200AuthAgentAcctSSH": me1200AuthAgentAcctSSH,
       "me1200AuthAgentAcctSSHMethod": me1200AuthAgentAcctSSHMethod,
       "me1200AuthAgentAcctSSHCmdEnable": me1200AuthAgentAcctSSHCmdEnable,
       "me1200AuthAgentAcctSSHCmdPrivLvl": me1200AuthAgentAcctSSHCmdPrivLvl,
       "me1200AuthAgentAcctSSHExecEnable": me1200AuthAgentAcctSSHExecEnable,
       "me1200AuthRADIUS": me1200AuthRADIUS,
       "me1200AuthRADIUSglobal": me1200AuthRADIUSglobal,
       "me1200AuthRADIUSglobalTimeout": me1200AuthRADIUSglobalTimeout,
       "me1200AuthRADIUSglobalRetransmit": me1200AuthRADIUSglobalRetransmit,
       "me1200AuthRADIUSglobalDeadtime": me1200AuthRADIUSglobalDeadtime,
       "me1200AuthRADIUSglobalKey": me1200AuthRADIUSglobalKey,
       "me1200AuthRADIUSconfig": me1200AuthRADIUSconfig,
       "me1200AuthRADIUSconfigNasIpv4Enable": me1200AuthRADIUSconfigNasIpv4Enable,
       "me1200AuthRADIUSconfigNasIpv4Address": me1200AuthRADIUSconfigNasIpv4Address,
       "me1200AuthRADIUSconfigNasIpv6Enable": me1200AuthRADIUSconfigNasIpv6Enable,
       "me1200AuthRADIUSconfigNasIpv6Address": me1200AuthRADIUSconfigNasIpv6Address,
       "me1200AuthRADIUSconfigNasIdentifier": me1200AuthRADIUSconfigNasIdentifier,
       "me1200AuthRADIUShostTable": me1200AuthRADIUShostTable,
       "me1200AuthRADIUShostEntry": me1200AuthRADIUShostEntry,
       "me1200AuthRADIUShostIndex": me1200AuthRADIUShostIndex,
       "me1200AuthRADIUShostAddress": me1200AuthRADIUShostAddress,
       "me1200AuthRADIUShostAuthPort": me1200AuthRADIUShostAuthPort,
       "me1200AuthRADIUShostAcctPort": me1200AuthRADIUShostAcctPort,
       "me1200AuthRADIUShostTimeout": me1200AuthRADIUShostTimeout,
       "me1200AuthRADIUShostRetransmit": me1200AuthRADIUShostRetransmit,
       "me1200AuthRADIUShostKey": me1200AuthRADIUShostKey,
       "me1200AuthTACACS": me1200AuthTACACS,
       "me1200AuthTACACSglobal": me1200AuthTACACSglobal,
       "me1200AuthTACACSglobalTimeout": me1200AuthTACACSglobalTimeout,
       "me1200AuthTACACSglobalDeadtime": me1200AuthTACACSglobalDeadtime,
       "me1200AuthTACACSglobalKey": me1200AuthTACACSglobalKey,
       "me1200AuthTACACShostTable": me1200AuthTACACShostTable,
       "me1200AuthTACACShostEntry": me1200AuthTACACShostEntry,
       "me1200AuthTACACShostIndex": me1200AuthTACACShostIndex,
       "me1200AuthTACACShostAddress": me1200AuthTACACShostAddress,
       "me1200AuthTACACShostAuthPort": me1200AuthTACACShostAuthPort,
       "me1200AuthTACACShostTimeout": me1200AuthTACACShostTimeout,
       "me1200AuthTACACShostKey": me1200AuthTACACShostKey,
       "me1200AuthMibConformance": me1200AuthMibConformance,
       "me1200AuthMibCompliances": me1200AuthMibCompliances,
       "me1200AuthMibCompliance": me1200AuthMibCompliance,
       "me1200AuthMibGroups": me1200AuthMibGroups,
       "me1200AuthAgentConsoleMethodsTableInfoGroup": me1200AuthAgentConsoleMethodsTableInfoGroup,
       "me1200AuthAgentTelnetMethodsTableInfoGroup": me1200AuthAgentTelnetMethodsTableInfoGroup,
       "me1200AuthAgentSSHMethodsTableInfoGroup": me1200AuthAgentSSHMethodsTableInfoGroup,
       "me1200AuthAgentHTTPMethodsTableInfoGroup": me1200AuthAgentHTTPMethodsTableInfoGroup,
       "me1200AuthAgentAuthorConsoleInfoGroup": me1200AuthAgentAuthorConsoleInfoGroup,
       "me1200AuthAgentAuthorTelnetInfoGroup": me1200AuthAgentAuthorTelnetInfoGroup,
       "me1200AuthAgentAuthorSSHInfoGroup": me1200AuthAgentAuthorSSHInfoGroup,
       "me1200AuthAgentAcctConsoleInfoGroup": me1200AuthAgentAcctConsoleInfoGroup,
       "me1200AuthAgentAcctTelnetInfoGroup": me1200AuthAgentAcctTelnetInfoGroup,
       "me1200AuthAgentAcctSSHInfoGroup": me1200AuthAgentAcctSSHInfoGroup,
       "me1200AuthRADIUSglobalInfoGroup": me1200AuthRADIUSglobalInfoGroup,
       "me1200AuthRADIUSconfigInfoGroup": me1200AuthRADIUSconfigInfoGroup,
       "me1200AuthRADIUShostTableInfoGroup": me1200AuthRADIUShostTableInfoGroup,
       "me1200AuthTACACSglobalInfoGroup": me1200AuthTACACSglobalInfoGroup,
       "me1200AuthTACACShostTableInfoGroup": me1200AuthTACACShostTableInfoGroup}
)
