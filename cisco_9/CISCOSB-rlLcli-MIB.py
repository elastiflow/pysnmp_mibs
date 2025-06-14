# SNMP MIB module (CISCOSB-rlLcli-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCOSB-rlLcli-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:13:48 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlLCli = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74)
)
if mibBuilder.loadTexts:
    rlLCli.setRevisions(
        ("2007-07-26 00:00",
         "2005-04-11 00:00",
         "2005-03-28 00:00",
         "2004-03-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlLCliMibVersion_Type = Integer32
_RlLCliMibVersion_Object = MibScalar
rlLCliMibVersion = _RlLCliMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 1),
    _RlLCliMibVersion_Type()
)
rlLCliMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLCliMibVersion.setStatus("current")


class _RlLCliTimeout_Type(Unsigned32):
    """Custom type rlLCliTimeout based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3932159),
    )


_RlLCliTimeout_Type.__name__ = "Unsigned32"
_RlLCliTimeout_Object = MibScalar
rlLCliTimeout = _RlLCliTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 2),
    _RlLCliTimeout_Type()
)
rlLCliTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLCliTimeout.setStatus("current")


class _RlLCliHistoryEnable_Type(TruthValue):
    """Custom type rlLCliHistoryEnable based on TruthValue"""
    defaultValue = 1


_RlLCliHistoryEnable_Type.__name__ = "TruthValue"
_RlLCliHistoryEnable_Object = MibScalar
rlLCliHistoryEnable = _RlLCliHistoryEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 3),
    _RlLCliHistoryEnable_Type()
)
rlLCliHistoryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLCliHistoryEnable.setStatus("current")


class _RlLCliHistorySize_Type(Unsigned32):
    """Custom type rlLCliHistorySize based on Unsigned32"""
    defaultValue = 10


_RlLCliHistorySize_Type.__name__ = "Unsigned32"
_RlLCliHistorySize_Object = MibScalar
rlLCliHistorySize = _RlLCliHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 4),
    _RlLCliHistorySize_Type()
)
rlLCliHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLCliHistorySize.setStatus("current")
_RlLcliCommandLevelTable_Object = MibTable
rlLcliCommandLevelTable = _RlLcliCommandLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 5)
)
if mibBuilder.loadTexts:
    rlLcliCommandLevelTable.setStatus("current")
_RlLcliCommandLevelEntry_Object = MibTableRow
rlLcliCommandLevelEntry = _RlLcliCommandLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 5, 1)
)
rlLcliCommandLevelEntry.setIndexNames(
    (0, "CISCOSB-rlLcli-MIB", "rlLcliCommandLevelCommandName"),
    (0, "CISCOSB-rlLcli-MIB", "rlLcliCommandLevelContextName"),
)
if mibBuilder.loadTexts:
    rlLcliCommandLevelEntry.setStatus("current")
_RlLcliCommandLevelCommandName_Type = DisplayString
_RlLcliCommandLevelCommandName_Object = MibTableColumn
rlLcliCommandLevelCommandName = _RlLcliCommandLevelCommandName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 5, 1, 1),
    _RlLcliCommandLevelCommandName_Type()
)
rlLcliCommandLevelCommandName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLcliCommandLevelCommandName.setStatus("current")
_RlLcliCommandLevelContextName_Type = DisplayString
_RlLcliCommandLevelContextName_Object = MibTableColumn
rlLcliCommandLevelContextName = _RlLcliCommandLevelContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 5, 1, 2),
    _RlLcliCommandLevelContextName_Type()
)
rlLcliCommandLevelContextName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLcliCommandLevelContextName.setStatus("current")
_RlLcliCommandLevelInsertTime_Type = TimeTicks
_RlLcliCommandLevelInsertTime_Object = MibTableColumn
rlLcliCommandLevelInsertTime = _RlLcliCommandLevelInsertTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 5, 1, 3),
    _RlLcliCommandLevelInsertTime_Type()
)
rlLcliCommandLevelInsertTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLcliCommandLevelInsertTime.setStatus("current")
_RlLcliCommandLevelCommandLevel_Type = Integer32
_RlLcliCommandLevelCommandLevel_Object = MibTableColumn
rlLcliCommandLevelCommandLevel = _RlLcliCommandLevelCommandLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 5, 1, 4),
    _RlLcliCommandLevelCommandLevel_Type()
)
rlLcliCommandLevelCommandLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLcliCommandLevelCommandLevel.setStatus("current")


class _RlLcliCommandLevelActionMode_Type(Integer32):
    """Custom type rlLcliCommandLevelActionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("reset", 2),
          ("setAll", 3),
          ("resetAll", 4))
    )


_RlLcliCommandLevelActionMode_Type.__name__ = "Integer32"
_RlLcliCommandLevelActionMode_Object = MibTableColumn
rlLcliCommandLevelActionMode = _RlLcliCommandLevelActionMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 5, 1, 5),
    _RlLcliCommandLevelActionMode_Type()
)
rlLcliCommandLevelActionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLcliCommandLevelActionMode.setStatus("current")
_RlLcliCommandLevelStatus_Type = RowStatus
_RlLcliCommandLevelStatus_Object = MibTableColumn
rlLcliCommandLevelStatus = _RlLcliCommandLevelStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 5, 1, 6),
    _RlLcliCommandLevelStatus_Type()
)
rlLcliCommandLevelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLcliCommandLevelStatus.setStatus("current")


class _RlLCliSshTimeout_Type(Unsigned32):
    """Custom type rlLCliSshTimeout based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3932159),
    )


_RlLCliSshTimeout_Type.__name__ = "Unsigned32"
_RlLCliSshTimeout_Object = MibScalar
rlLCliSshTimeout = _RlLCliSshTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 6),
    _RlLCliSshTimeout_Type()
)
rlLCliSshTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLCliSshTimeout.setStatus("current")


class _RlLCliTelnetTimeout_Type(Unsigned32):
    """Custom type rlLCliTelnetTimeout based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3932159),
    )


_RlLCliTelnetTimeout_Type.__name__ = "Unsigned32"
_RlLCliTelnetTimeout_Object = MibScalar
rlLCliTelnetTimeout = _RlLCliTelnetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 7),
    _RlLCliTelnetTimeout_Type()
)
rlLCliTelnetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLCliTelnetTimeout.setStatus("current")


class _RlLCliTelnetHistoryEnable_Type(TruthValue):
    """Custom type rlLCliTelnetHistoryEnable based on TruthValue"""
    defaultValue = 1


_RlLCliTelnetHistoryEnable_Type.__name__ = "TruthValue"
_RlLCliTelnetHistoryEnable_Object = MibScalar
rlLCliTelnetHistoryEnable = _RlLCliTelnetHistoryEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 8),
    _RlLCliTelnetHistoryEnable_Type()
)
rlLCliTelnetHistoryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLCliTelnetHistoryEnable.setStatus("current")


class _RlLCliTelnetHistorySize_Type(Unsigned32):
    """Custom type rlLCliTelnetHistorySize based on Unsigned32"""
    defaultValue = 10


_RlLCliTelnetHistorySize_Type.__name__ = "Unsigned32"
_RlLCliTelnetHistorySize_Object = MibScalar
rlLCliTelnetHistorySize = _RlLCliTelnetHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 9),
    _RlLCliTelnetHistorySize_Type()
)
rlLCliTelnetHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLCliTelnetHistorySize.setStatus("current")


class _RlLCliSshHistoryEnable_Type(TruthValue):
    """Custom type rlLCliSshHistoryEnable based on TruthValue"""
    defaultValue = 1


_RlLCliSshHistoryEnable_Type.__name__ = "TruthValue"
_RlLCliSshHistoryEnable_Object = MibScalar
rlLCliSshHistoryEnable = _RlLCliSshHistoryEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 10),
    _RlLCliSshHistoryEnable_Type()
)
rlLCliSshHistoryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLCliSshHistoryEnable.setStatus("current")


class _RlLCliSshHistorySize_Type(Unsigned32):
    """Custom type rlLCliSshHistorySize based on Unsigned32"""
    defaultValue = 10


_RlLCliSshHistorySize_Type.__name__ = "Unsigned32"
_RlLCliSshHistorySize_Object = MibScalar
rlLCliSshHistorySize = _RlLCliSshHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 74, 11),
    _RlLCliSshHistorySize_Type()
)
rlLCliSshHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLCliSshHistorySize.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-rlLcli-MIB",
    **{"rlLCli": rlLCli,
       "rlLCliMibVersion": rlLCliMibVersion,
       "rlLCliTimeout": rlLCliTimeout,
       "rlLCliHistoryEnable": rlLCliHistoryEnable,
       "rlLCliHistorySize": rlLCliHistorySize,
       "rlLcliCommandLevelTable": rlLcliCommandLevelTable,
       "rlLcliCommandLevelEntry": rlLcliCommandLevelEntry,
       "rlLcliCommandLevelCommandName": rlLcliCommandLevelCommandName,
       "rlLcliCommandLevelContextName": rlLcliCommandLevelContextName,
       "rlLcliCommandLevelInsertTime": rlLcliCommandLevelInsertTime,
       "rlLcliCommandLevelCommandLevel": rlLcliCommandLevelCommandLevel,
       "rlLcliCommandLevelActionMode": rlLcliCommandLevelActionMode,
       "rlLcliCommandLevelStatus": rlLcliCommandLevelStatus,
       "rlLCliSshTimeout": rlLCliSshTimeout,
       "rlLCliTelnetTimeout": rlLCliTelnetTimeout,
       "rlLCliTelnetHistoryEnable": rlLCliTelnetHistoryEnable,
       "rlLCliTelnetHistorySize": rlLCliTelnetHistorySize,
       "rlLCliSshHistoryEnable": rlLCliSshHistoryEnable,
       "rlLCliSshHistorySize": rlLCliSshHistorySize}
)
